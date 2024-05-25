import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';
import { jupyterFaviconIcon } from '@jupyterlab/ui-components';


import logoIconStr  from '../style/icons/logo.svg';

/**
 * Initialization data for the minerva-tech-theme extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'minerva-tech-theme:plugin',
  description: 'A JupyterLab Theme for the MinervaTechnologies.',
  autoStart: true,
  requires: [IThemeManager],
  activate: (app: JupyterFrontEnd, manager: IThemeManager) => {
    console.log('JupyterLab extension minerva-tech-theme is activated!');
    const style = 'minerva-tech-theme/index.css';

    console.log(logoIconStr);
    jupyterFaviconIcon.svgstr = logoIconStr;
    

    manager.register({
      name: 'minerva-tech-theme',
      isLight: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  }
};

export default plugin;
