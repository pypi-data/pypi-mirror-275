/*
 **  Copyright (C) Optumi Inc - All rights reserved.
 **
 **  You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
 **  To receive a copy of the licensing terms please write to contact@optumi.com or visit us at http://www.optumi.com.
 **/

import * as React from 'react';
import { Global } from 'common';

import { JupyterFrontEnd, JupyterFrontEndPlugin, ILabShell, ILayoutRestorer } from '@jupyterlab/application';
import { ServerConnection } from '@jupyterlab/services';
import { IDocumentManager } from '@jupyterlab/docmanager';
import { ReactWidget, IThemeManager } from '@jupyterlab/apputils';
import { Token } from '@lumino/coreutils';
import { Widget } from '@lumino/widgets';

import { LabIcon } from '@jupyterlab/ui-components';

import { OptumiLeftPanel, JupyterlabProgramTracker } from 'common';

// TODO:JJ Does this really need to be exported?
export const IOptumi = new Token<IOptumi>('optumi:IOptumi');

// TODO:JJ Does this really need to be exported?
export interface IOptumi {
    widget: Widget;
}

const id = 'optumi';

export default {
    activate,
    id,
    requires: [ILabShell, ILayoutRestorer, IThemeManager, IDocumentManager],
    provides: IOptumi,
    autoStart: true,
} as JupyterFrontEndPlugin<void>;

async function activate(
    lab: JupyterFrontEnd,
    labShell: ILabShell,
    restorer: ILayoutRestorer,
    manager: IThemeManager,
    docManager: IDocumentManager,
) {
    // Creates the left side bar widget once the app has fully started
    lab.started.then(async () => {
        document.documentElement.style.setProperty('--jp-sidebar-min-width', '340px');
        // Set some well known globals
        Global.lab = lab;
        Global.labShell = labShell;
        Global.programTracker = new JupyterlabProgramTracker(labShell);
        Global.themeManager = manager;
        Global.docManager = docManager;
        Global.agreementURL = await docManager.services.contents.getDownloadUrl('Agreement.html');

        // Wait until we have a version to set metadata related globals
        const settings = ServerConnection.makeSettings();
        const url = settings.baseUrl + 'optumi/version';
        const response = await ServerConnection.makeRequest(url, {}, settings);
        if (response.status !== 200) throw new ServerConnection.ResponseError(response);

        const data = await response.json();
        // Get the version from the server
        // We do not want to start the extension until we know the version, it might mess with metadata
        const version = data.version;
        const userHome = data.userHome;
        const jupyterHome = data.jupyterHome;

        console.log('JupyterLab extension jupyterlab-optumi version ' + version + ' is activated!');

        Global.version = version;
        Global.userHome = userHome;
        Global.jupyterHome = jupyterHome;

        const widget = ReactWidget.create(<OptumiLeftPanel />);
        widget.id = 'optumi/Optumi';
        // This is a hack to stop jupyterlab from showing a default icon above our optumi logo
        widget.title.icon = new LabIcon({
            name: 'empty',
            svgstr: '<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" width="1" height="1"/>',
        });
        widget.title.iconClass = 'jp-o-logo jp-SideBar-tabIcon';
        widget.title.caption = 'Optumi';

        restorer.add(widget, widget.id);

        // Initialize once the application shell has been restored
        lab.restored.then(() => {
            // add widget
            if (!widget.isAttached) {
                labShell.add(widget, 'left', { rank: 1000 });
            }
        });
    });
}
