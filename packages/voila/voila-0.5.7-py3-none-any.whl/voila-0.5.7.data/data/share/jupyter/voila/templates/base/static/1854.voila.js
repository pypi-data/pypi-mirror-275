"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[1854,4235],{66616:(e,n,s)=>{s.r(n),s.d(n,{EditMenu:()=>d,FileMenu:()=>m,HelpMenu:()=>o,IMainMenu:()=>k,KernelMenu:()=>c,MainMenu:()=>p,RunMenu:()=>l,SettingsMenu:()=>M,TabsMenu:()=>h,ViewMenu:()=>_});var t,r=s(76608),i=s(39296),a=s(61384),u=s(91804);class d extends r.RankedMenu{constructor(e){super(e),this.undoers={redo:new u.SemanticCommand,undo:new u.SemanticCommand},this.clearers={clearAll:new u.SemanticCommand,clearCurrent:new u.SemanticCommand},this.goToLiners=new u.SemanticCommand}}class m extends r.RankedMenu{constructor(e){super(e),this.quitEntry=!1,this.closeAndCleaners=new u.SemanticCommand,this.consoleCreators=new u.SemanticCommand}get newMenu(){var e,n;return this._newMenu||(this._newMenu=null!==(n=null===(e=(0,i.find)(this.items,(e=>{var n;return"jp-mainmenu-file-new"===(null===(n=e.submenu)||void 0===n?void 0:n.id)})))||void 0===e?void 0:e.submenu)&&void 0!==n?n:new r.RankedMenu({commands:this.commands})),this._newMenu}dispose(){var e;null===(e=this._newMenu)||void 0===e||e.dispose(),super.dispose()}}class o extends r.RankedMenu{constructor(e){super(e),this.getKernel=new u.SemanticCommand}}class c extends r.RankedMenu{constructor(e){super(e),this.kernelUsers={changeKernel:new u.SemanticCommand,clearWidget:new u.SemanticCommand,interruptKernel:new u.SemanticCommand,reconnectToKernel:new u.SemanticCommand,restartKernel:new u.SemanticCommand,shutdownKernel:new u.SemanticCommand}}}class l extends r.RankedMenu{constructor(e){super(e),this.codeRunners={restart:new u.SemanticCommand,run:new u.SemanticCommand,runAll:new u.SemanticCommand}}}class M extends r.RankedMenu{constructor(e){super(e)}}class h extends r.RankedMenu{constructor(e){super(e)}}class _ extends r.RankedMenu{constructor(e){super(e),this.editorViewers={toggleLineNumbers:new u.SemanticCommand,toggleMatchBrackets:new u.SemanticCommand,toggleWordWrap:new u.SemanticCommand}}}class p extends a.MenuBar{constructor(e){super({forceItemsPosition:{forceX:!1,forceY:!0}}),this._items=[],this._commands=e}get editMenu(){return this._editMenu||(this._editMenu=new d({commands:this._commands,rank:2,renderer:r.MenuSvg.defaultRenderer})),this._editMenu}get fileMenu(){return this._fileMenu||(this._fileMenu=new m({commands:this._commands,rank:1,renderer:r.MenuSvg.defaultRenderer})),this._fileMenu}get helpMenu(){return this._helpMenu||(this._helpMenu=new o({commands:this._commands,rank:1e3,renderer:r.MenuSvg.defaultRenderer})),this._helpMenu}get kernelMenu(){return this._kernelMenu||(this._kernelMenu=new c({commands:this._commands,rank:5,renderer:r.MenuSvg.defaultRenderer})),this._kernelMenu}get runMenu(){return this._runMenu||(this._runMenu=new l({commands:this._commands,rank:4,renderer:r.MenuSvg.defaultRenderer})),this._runMenu}get settingsMenu(){return this._settingsMenu||(this._settingsMenu=new M({commands:this._commands,rank:999,renderer:r.MenuSvg.defaultRenderer})),this._settingsMenu}get viewMenu(){return this._viewMenu||(this._viewMenu=new _({commands:this._commands,rank:3,renderer:r.MenuSvg.defaultRenderer})),this._viewMenu}get tabsMenu(){return this._tabsMenu||(this._tabsMenu=new h({commands:this._commands,rank:500,renderer:r.MenuSvg.defaultRenderer})),this._tabsMenu}addMenu(e,n=!0,s={}){if(i.ArrayExt.firstIndexOf(this.menus,e)>-1)return;r.MenuSvg.overrideDefaultRenderer(e);const a={menu:e,rank:"rank"in s?s.rank:"rank"in e?e.rank:r.IRankedMenu.DEFAULT_RANK},u=i.ArrayExt.upperBound(this._items,a,t.itemCmp);switch(e.disposed.connect(this._onMenuDisposed,this),i.ArrayExt.insert(this._items,u,a),this.insertMenu(u,e),e.id){case"jp-mainmenu-file":!this._fileMenu&&e instanceof m&&(this._fileMenu=e);break;case"jp-mainmenu-edit":!this._editMenu&&e instanceof d&&(this._editMenu=e);break;case"jp-mainmenu-view":!this._viewMenu&&e instanceof _&&(this._viewMenu=e);break;case"jp-mainmenu-run":!this._runMenu&&e instanceof l&&(this._runMenu=e);break;case"jp-mainmenu-kernel":!this._kernelMenu&&e instanceof c&&(this._kernelMenu=e);break;case"jp-mainmenu-tabs":!this._tabsMenu&&e instanceof h&&(this._tabsMenu=e);break;case"jp-mainmenu-settings":!this._settingsMenu&&e instanceof M&&(this._settingsMenu=e);break;case"jp-mainmenu-help":!this._helpMenu&&e instanceof o&&(this._helpMenu=e)}}dispose(){var e,n,s,t,r,i,a,u;null===(e=this._editMenu)||void 0===e||e.dispose(),null===(n=this._fileMenu)||void 0===n||n.dispose(),null===(s=this._helpMenu)||void 0===s||s.dispose(),null===(t=this._kernelMenu)||void 0===t||t.dispose(),null===(r=this._runMenu)||void 0===r||r.dispose(),null===(i=this._settingsMenu)||void 0===i||i.dispose(),null===(a=this._viewMenu)||void 0===a||a.dispose(),null===(u=this._tabsMenu)||void 0===u||u.dispose(),super.dispose()}static generateMenu(e,n,s){let t;const{id:i,label:a,rank:u}=n;switch(i){case"jp-mainmenu-file":t=new m({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer});break;case"jp-mainmenu-edit":t=new d({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer});break;case"jp-mainmenu-view":t=new _({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer});break;case"jp-mainmenu-run":t=new l({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer});break;case"jp-mainmenu-kernel":t=new c({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer});break;case"jp-mainmenu-tabs":t=new h({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer});break;case"jp-mainmenu-settings":t=new M({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer});break;case"jp-mainmenu-help":t=new o({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer});break;default:t=new r.RankedMenu({commands:e,rank:u,renderer:r.MenuSvg.defaultRenderer})}return a&&(t.title.label=s._p("menu",a)),t}_onMenuDisposed(e){this.removeMenu(e);const n=i.ArrayExt.findFirstIndex(this._items,(n=>n.menu===e));-1!==n&&i.ArrayExt.removeAt(this._items,n)}}!function(e){e.itemCmp=function(e,n){return e.rank-n.rank}}(t||(t={}));const k=new(s(11296).Token)("@jupyterlab/mainmenu:IMainMenu","A service for the main menu bar for the application.\n  Use this if you want to add your own menu items or provide implementations for standardized menu items for specific activities.")}}]);