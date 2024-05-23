"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[144,8832,9296,5672,6296,1384,1077,3516,9548],{91216:(e,t,n)=>{n.d(t,{c:()=>s});var i=n(75004),r=n.n(i),o=n(35811),a=n.n(o)()(r());a.push([e.id,"body {\n  padding: 0 !important;\n}\ndiv#main {\n  height: 100vh;\n  background-color: var(--jp-layout-color2);\n}\ndiv#rendered_cells {\n  background-color: var(--jp-layout-color1);\n}\ndiv#voila-top-panel {\n  min-height: var(--jp-private-menubar-height);\n  display: flex;\n}\ndiv#voila-bottom-panel {\n  min-height: var(--jp-private-menubar-height);\n  display: flex;\n}\ndiv#rendered_cells {\n  padding: var(--jp-notebook-padding);\n  overflow: auto;\n}\n\n.voila-FileBrowser {\n  max-width: 1000px;\n  box-shadow: var(--jp-elevation-z4);\n}\n\n.voila-FileBrowser .jp-DirListing-item {\n  border-bottom-style: solid;\n  border-bottom-width: var(--jp-border-width);\n  border-bottom-color: var(--jp-border-color0);\n  padding: 10px 12px;\n}\n\n.voila-FileBrowser .jp-DirListing-itemText:focus {\n  outline-style: none;\n}\n\n.spacer-top-widget {\n  max-height: 50px;\n}\n\n.spacer-bottom-widget {\n  max-height: 50px;\n}\n",""]);const s=a},43416:(e,t,n)=>{n.r(t),n(75080),n(8792),n(8096),n(10496),n(68288),n(23884),n(23816),n(76344);var i=n(58080),r=n.n(i),o=n(76984),a=n.n(o),s=n(53404),l=n.n(s),d=n(54760),h=n.n(d),u=n(33416),c=n.n(u),g=n(38396),p=n.n(g),m=n(91216),A={};A.styleTagTransform=p(),A.setAttributes=h(),A.insert=l().bind(null,"head"),A.domAPI=a(),A.insertStyleElement=c(),r()(m.c,A),m.c&&m.c.locals&&m.c.locals;var w,v=n(39128),y=n(56125),b=n(11296),f=n(82100),_=n(39296),P=n(53516),j=n(64456),C=n(43884),S=n(61384);class x extends S.Widget{constructor(){super(),this._layoutDebouncer=new j.Debouncer((()=>{this._layoutModified.emit(void 0)}),0),this._layoutModified=new C.Signal(this),this.id="main";const e=new S.BoxLayout;e.alignment="start",e.spacing=0,this.addClass("jp-LabShell");const t=this._topHandler=new w.PanelHandler;t.panel.id="voila-top-panel",t.panel.node.setAttribute("role","banner"),S.BoxLayout.setStretch(t.panel,0),t.panel.hide(),e.addWidget(t.panel);const n=this._mainPanel=new S.BoxPanel;n.id="jp-main-content-panel",n.direction="top-to-bottom",S.BoxLayout.setStretch(n,1),e.addWidget(n);const i=this._bottomPanel=new S.Panel;i.node.setAttribute("role","contentinfo"),i.id="voila-bottom-panel",S.BoxLayout.setStretch(i,0),e.addWidget(i),i.hide(),this.layout=e}get currentWidget(){return this._mainPanel.widgets[0]}activateById(e){}add(e,t,n){switch(t){case"top":this._addToTopArea(e,n);break;case"bottom":this._addToBottomArea(e,n);break;case"main":this._mainPanel.addWidget(e);break;default:console.warn(`Area ${t} is not implemented yet!`)}}widgets(e){switch(e){case"top":return this._topHandler.panel.children();case"bottom":return this._bottomPanel.children();case"main":this._mainPanel.children();break;default:return[][Symbol.iterator]()}return[][Symbol.iterator]()}_addToTopArea(e,t){var n;if(!e.id)return void console.error("Widgets added to app shell must have unique id property.");const i=null!==(n=(t=t||{}).rank)&&void 0!==n?n:900;this._topHandler.addWidget(e,i),this._onLayoutModified(),this._topHandler.panel.isHidden&&this._topHandler.panel.show()}_addToBottomArea(e,t){e.id?(this._bottomPanel.addWidget(e),this._onLayoutModified(),this._bottomPanel.isHidden&&this._bottomPanel.show()):console.error("Widgets added to app shell must have unique id property.")}_onLayoutModified(){this._layoutDebouncer.invoke()}}!function(e){e.itemCmp=function(e,t){return e.rank-t.rank},e.PanelHandler=class{constructor(){this._panelChildHook=(e,t)=>{switch(t.type){case"child-added":{const e=t.child;if(this._items.find((t=>t.widget===e)))break;const n=this._items[this._items.length-1].rank;this._items.push({widget:e,rank:n})}break;case"child-removed":{const e=t.child;_.ArrayExt.removeFirstWhere(this._items,(t=>t.widget===e))}}return!0},this._items=new Array,this._panel=new S.Panel,P.MessageLoop.installMessageHook(this._panel,this._panelChildHook)}get panel(){return this._panel}addWidget(t,n){t.parent=null;const i={widget:t,rank:n},r=_.ArrayExt.upperBound(this._items,i,e.itemCmp);_.ArrayExt.insert(this._items,r,i),this._panel.insertWidget(r,t)}}}(w||(w={}));const k=n(56604);class E extends f.JupyterFrontEnd{constructor(e){var t;if(super(Object.assign(Object.assign({},e),{shell:null!==(t=e.shell)&&void 0!==t?t:new x})),this.name="Voila",this.namespace=this.name,this.version=k.version,this._widgetManager=null,this._widgetManagerPromise=new b.PromiseDelegate,e.mimeExtensions)for(const t of(0,f.createRendermimePlugins)(e.mimeExtensions))this.registerPlugin(t)}get paths(){return{urls:{base:v.PageConfig.getOption("baseUrl"),notFound:v.PageConfig.getOption("notFoundUrl"),app:v.PageConfig.getOption("appUrl"),static:v.PageConfig.getOption("staticUrl"),settings:v.PageConfig.getOption("settingsUrl"),themes:v.PageConfig.getOption("themesUrl"),doc:v.PageConfig.getOption("docUrl"),translations:v.PageConfig.getOption("translationsApiUrl"),hubHost:v.PageConfig.getOption("hubHost")||void 0,hubPrefix:v.PageConfig.getOption("hubPrefix")||void 0,hubUser:v.PageConfig.getOption("hubUser")||void 0,hubServerName:v.PageConfig.getOption("hubServerName")||void 0},directories:{appSettings:v.PageConfig.getOption("appSettingsDir"),schemas:v.PageConfig.getOption("schemasDir"),static:v.PageConfig.getOption("staticDir"),templates:v.PageConfig.getOption("templatesDir"),themes:v.PageConfig.getOption("themesDir"),userSettings:v.PageConfig.getOption("userSettingsDir"),serverRoot:v.PageConfig.getOption("serverRoot"),workspaces:v.PageConfig.getOption("workspacesDir")}}}registerPluginModule(e){let t=e.default;Object.prototype.hasOwnProperty.call(e,"__esModule")||(t=e),Array.isArray(t)||(t=[t]),t.forEach((e=>{try{this.registerPlugin(e)}catch(e){console.error(e)}}))}registerPluginModules(e){e.forEach((e=>{this.registerPluginModule(e)}))}get widgetManagerPromise(){return this._widgetManagerPromise}set widgetManager(e){this._widgetManager=e,this._widgetManager&&this._widgetManagerPromise.resolve(this._widgetManager)}get widgetManager(){return this._widgetManager}}var O=n(17116),M=n(9428),T=n(88480),L=n(89968),U=n(80164),F=n(91804);class R extends U._{get urlFactory(){return this._urlFactory}set urlFactory(e){this._urlFactory=e}handleOpen(e){if("directory"===e.type){const t=this.model.manager.services.contents.localPath(e.path);this.model.cd(`/${t}`).catch((e=>(0,F.showErrorMessage)("Open directory",e)))}else{const t=e.path;this.urlFactory?window.open(this.urlFactory(t),"_blank"):(0,F.showErrorMessage)("Open file","URL Factory is not defined")}}handleEvent(e){"click"===e.type&&this.evtDblClick(e)}}class B extends L.k{constructor(e){const{urlFactory:t,title:n}=e;super(function(e,t){var n={};for(var i in e)Object.prototype.hasOwnProperty.call(e,i)&&t.indexOf(i)<0&&(n[i]=e[i]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var r=0;for(i=Object.getOwnPropertySymbols(e);r<i.length;r++)t.indexOf(i[r])<0&&Object.prototype.propertyIsEnumerable.call(e,i[r])&&(n[i[r]]=e[i[r]])}return n}(e,["urlFactory","title"])),this.listing.urlFactory=t,this.addClass("voila-FileBrowser");const i=new S.Widget;i.node.innerText=n,this.toolbar.addItem("title",i)}createDirListing(e){return new R(e)}}const D={id:"@voila-dashboards/voila:tree-widget",description:"Provides the file browser.",activate:e=>{const t=new M.DocumentRegistry,n=new O.g({registry:t,manager:e.serviceManager,opener}),i=new T.G2({manager:n,refreshInterval:2147483646}),r=new B({id:"filebrowser",model:i,urlFactory:e=>{const t=v.PageConfig.getBaseUrl(),n=v.PageConfig.getOption("frontend"),i=v.PageConfig.getOption("query");return v.URLExt.join(t,n,"render",e)+`?${i}`},title:"Select items to open with Voilà."});r.showFileCheckboxes=!1,r.showLastModifiedColumn=!1;const o=new S.Widget;o.addClass("spacer-top-widget"),e.shell.add(o,"main"),e.shell.add(r,"main");const a=new S.Widget;a.addClass("spacer-bottom-widget"),e.shell.add(a,"main")},autoStart:!0};class W extends y.EventManager{constructor(e={}){super(e),this.dispose()}}class I extends y.BaseManager{constructor(){super(...arguments),this.userChanged=new C.Signal(this),this.connectionFailure=new C.Signal(this),this.identity=null,this.permissions=null}refreshUser(){return Promise.resolve()}get isReady(){return!0}get ready(){return Promise.resolve()}}class $ extends y.BaseManager{constructor(){super(...arguments),this.specsChanged=new C.Signal(this),this.connectionFailure=new C.Signal(this),this.specs=null}refreshSpecs(){return Promise.resolve()}get isReady(){return!0}get ready(){return Promise.resolve()}}const H=()=>!0;class V extends y.ServiceManager{constructor(e){var t,n,i,r,o;super({standby:null!==(t=null==e?void 0:e.standby)&&void 0!==t?t:H,kernelspecs:null!==(n=null==e?void 0:e.kernelspecs)&&void 0!==n?n:new $({}),events:null!==(i=null==e?void 0:e.events)&&void 0!==i?i:new W,user:null!==(r=null==e?void 0:e.user)&&void 0!==r?r:new I({}),contents:null!==(o=null==e?void 0:e.contents)&&void 0!==o?o:new y.ContentsManager})}}async function J(e,t){try{return(await window._JUPYTERLAB[e].get(t))()}catch(n){throw console.warn(`Failed to create module: package: ${e}; module: ${t}`),n}}function*q(e,t){let n;n=Object.prototype.hasOwnProperty.call(e,"__esModule")?e.default:e;const i=Array.isArray(n)?n:[n];for(const e of i)v.PageConfig.Extension.isDisabled(e.id)||t.includes(e.id)||t.includes(e.id.split(":")[0])||(yield e)}const N={id:"@voila-dashboards/voila:paths",activate:e=>e.paths,autoStart:!0,provides:f.JupyterFrontEnd.IPaths};var K=n(4956);const Y={id:"@voila-dashboards/voila:translator",activate:e=>new K.TranslationManager,autoStart:!0,provides:K.ITranslator};var z=n(89220),Q=n(77232),G=n(16024),Z=n(69928);S.Widget;const X="application/vnd.jupyter.widget-view+json",ee={id:"@voila-dashboards/voila:widget-manager",autoStart:!0,requires:[z.IRenderMimeRegistry],provides:Z.IJupyterWidgetRegistry,activate:async(e,t)=>{if(!(e instanceof E))throw Error("The Voila Widget Manager plugin must be activated in a VoilaApp");const n=v.PageConfig.getBaseUrl(),i=v.PageConfig.getOption("kernelId"),r=y.ServerConnection.makeSettings({baseUrl:n}),o=await y.KernelAPI.getKernelModel(i,r);if(!o)return{registerWidget(e){throw Error(`The model for kernel id ${i} does not exist`)}};const a=new Q.KernelConnection({model:o,serverSettings:r}),s=new G.KernelWidgetManager(a,t);return e.widgetManager=s,t.removeMimeType(X),t.addFactory({safe:!1,mimeTypes:[X],createRenderer:e=>new G.WidgetRenderer(e,s)},-10),window.addEventListener("beforeunload",(e=>{const t=new FormData,i=document.cookie.match("\\b_xsrf=([^;]*)\\b"),r=i&&i[1]||"";t.append("_xsrf",r),window.navigator.sendBeacon(`${n}voila/api/shutdown/${a.id}`,t),a.dispose()})),{registerWidget:async t=>{(await e.widgetManagerPromise.promise).register(t)}}}};z.IRenderMimeRegistry,Z.IJupyterWidgetRegistry;var te=n(98564),ne=n(87716),ie=n(48832);const re="JupyterLab Light";class oe{constructor(e){this._current=null,this._links=[],this._overrides={},this._overrideProps={},this._outstanding=null,this._pending=0,this._requests={},this._themes={},this._themeChanged=new C.Signal(this),this._requestedTheme=re;const{host:t,url:n}=e;this.translator=e.translator||K.nullTranslator,this._trans=this.translator.load("jupyterlab"),this._base=n,this._host=t}get theme(){return this._current}get themes(){return Object.keys(this._themes)}get themeChanged(){return this._themeChanged}getCSS(e){var t;return null!==(t=this._overrides[e])&&void 0!==t?t:getComputedStyle(document.documentElement).getPropertyValue(`--jp-${e}`)}loadCSS(e){const t=this._base,n=v.URLExt.isLocal(e)?v.URLExt.join(t,e):e,i=this._links;return new Promise(((e,t)=>{const r=document.createElement("link");r.setAttribute("rel","stylesheet"),r.setAttribute("type","text/css"),r.setAttribute("href",n),r.addEventListener("load",(()=>{e(void 0)})),r.addEventListener("error",(()=>{t(`Stylesheet failed to load: ${n}`)})),document.body.appendChild(r),i.push(r),this.loadCSSOverrides()}))}loadCSSOverrides(){this._overrides={}}validateCSS(e,t){const n=this._overrideProps[e];return n?!!CSS.supports(n,t)||(console.warn(`CSS validation failed: invalid value.\nkey: '${e}', val: '${t}', prop: '${n}'`),!1):(console.warn(`CSS validation failed: could not find property corresponding to key.\nkey: '${e}', val: '${t}'`),!1)}register(e){const{name:t}=e,n=this._themes;if(n[t])throw new Error(`Theme already registered for ${t}`);return n[t]=e,this._themeChanged.emit({name:"",oldValue:null,newValue:""}),new ie.DisposableDelegate((()=>{delete n[t]}))}async setTheme(e){this._requestedTheme=e,this._loadSettings()}isLight(e){return this._themes[e].isLight}themeScrollbars(e){return!1}getDisplayName(e){var t,n;return null!==(n=null===(t=this._themes[e])||void 0===t?void 0:t.displayName)&&void 0!==n?n:e}_loadSettings(){const e=this._outstanding,t=this._pending,n=this._requests;t&&(window.clearTimeout(t),this._pending=0);const i=this._themes,r=this._requestedTheme;if(e)return e.then((()=>{this._loadSettings()})).catch((()=>{this._loadSettings()})),void(this._outstanding=null);if(n[r]=n[r]?n[r]+1:1,i[r])return this._outstanding=this._loadTheme(r),void delete n[r];if(n[r]>20){const e=re;return delete n[r],i[e]?(console.warn(`Could not load theme ${r}, using default ${e}.`),void(this._outstanding=this._loadTheme(e))):void this._onError(this._trans.__("Neither theme %1 nor default %2 loaded.",r,e))}this._pending=window.setTimeout((()=>{this._loadSettings()}),75)}_loadTheme(e){const t=this._current,n=this._links,i=this._themes,r=new ie.DisposableDelegate((()=>{}));n.forEach((e=>{e.parentElement&&e.parentElement.removeChild(e)})),n.length=0;const o=t?i[t].unload():Promise.resolve();return Promise.all([o,i[e].load()]).then((()=>{this._current=e,this._themeChanged.emit({name:"theme",oldValue:t,newValue:e}),this._host&&(this._host.hide(),requestAnimationFrame((()=>{this._host.show(),ae.fitAll(this._host),r.dispose()})))})).catch((e=>{this._onError(e),r.dispose()}))}_onError(e){(0,F.showDialog)({title:this._trans.__("Error Loading Theme"),body:String(e),buttons:[F.Dialog.okButton({label:this._trans.__("OK")})]})}}var ae;!function(e){e.fitAll=function e(t){for(const n of t.children())e(n);t.fit()}}(ae||(ae={}));const se={id:"@voila-dashboards/voila:theme-manager",description:"Provides the theme manager.",requires:[f.JupyterFrontEnd.IPaths],activate:(e,t)=>{const n=e.shell,i=v.URLExt.join(v.PageConfig.getBaseUrl(),t.urls.themes),r=new oe({host:n,url:i});let o;return r.themeChanged.connect(((e,t)=>{o=t.newValue,o.length>0&&(document.body.dataset.jpThemeLight=String(r.isLight(o)),document.body.dataset.jpThemeName=o)})),r},autoStart:!0,provides:F.IThemeManager},le={id:"@voila-dashboards/voila:theme",autoStart:!0,optional:[F.IThemeManager],activate:async(e,t)=>{if(ne.jupyterHighlightStyle.module&&te.StyleModule.mount(document,ne.jupyterHighlightStyle.module),!t)return;const n=v.PageConfig.getOption("jupyterLabTheme")||"light";"dark"!==n&&"light"!==n&&await t.setTheme(n),window.themeLoaded=!0,window.cellLoaded&&window.voila_finish()}};window.addEventListener("load",(async function(){const e=[n(60484),n(97596),n(86780),N,Y,le,ee,se,D],t=[],i=JSON.parse(v.PageConfig.getOption("federated_extensions")),r=[],o=[],a=[];(await Promise.allSettled(i.map((async e=>(await async function(e,t){await function(e){return new Promise(((t,n)=>{const i=document.createElement("script");i.onerror=n,i.onload=t,i.async=!0,document.head.appendChild(i),i.src=e}))}(e),await n.I("default");const i=window._JUPYTERLAB[t];await i.init(n.S.default)}(`${v.URLExt.join(v.PageConfig.getOption("fullLabextensionsUrl"),e.name,e.load)}`,e.name),e))))).forEach((e=>{if("rejected"===e.status)return void console.error(e.reason);const t=e.value;t.extension&&r.push(J(t.name,t.extension)),t.mimeExtension&&o.push(J(t.name,t.mimeExtension)),t.style&&a.push(J(t.name,t.style))})),(await Promise.allSettled(r)).forEach((t=>{if("fulfilled"===t.status)for(const n of q(t.value,[]))e.push(n);else console.error(t.reason)})),(await Promise.allSettled(o)).forEach((e=>{if("fulfilled"===e.status)for(const n of q(e.value,[]))t.push(n);else console.error(e.reason)})),(await Promise.allSettled(a)).filter((({status:e})=>"rejected"===e)).forEach((e=>{console.error(e.reason)}));const s=new y.Drive({apiEndpoint:"voila/api/contents"}),l=new y.ContentsManager({defaultDrive:s}),d=new E({mimeExtensions:t,shell:new x,serviceManager:new V({contents:l})});d.registerPluginModules(e),d.started.then((()=>{const e=document.getElementById("voila-tree-main");e&&(e.style.display="unset")})),await d.start()}))},55880:e=>{e.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII="},56604:e=>{e.exports=JSON.parse('{"name":"@voila-dashboards/voila","version":"0.5.7","description":"The Voilà Frontend","author":"Voilà contributors","license":"BSD-3-Clause","main":"lib/index.js","repository":{"type":"git","url":"https://github.com/voila-dashboards/voila"},"browserslist":">0.8%, not ie 11, not op_mini all, not dead","dependencies":{"@jupyter-widgets/base":"^6.0.6","@jupyter-widgets/jupyterlab-manager":"^5.0.9","@jupyterlab/application":"^4.0.0","@jupyterlab/apputils":"^4.0.0","@jupyterlab/apputils-extension":"^4.0.0","@jupyterlab/codemirror":"^4.0.3","@jupyterlab/codemirror-extension":"^4.0.0","@jupyterlab/coreutils":"^6.0.0","@jupyterlab/docregistry":"^4.0.0","@jupyterlab/javascript-extension":"^4.0.0","@jupyterlab/json-extension":"^4.0.0","@jupyterlab/logconsole":"^4.0.0","@jupyterlab/mainmenu":"^4.0.0","@jupyterlab/markedparser-extension":"^4.0.0","@jupyterlab/mathjax-extension":"^4.0.0","@jupyterlab/mathjax2-extension":"^4.0.0","@jupyterlab/nbformat":"^4.0.0","@jupyterlab/notebook":"^4.0.0","@jupyterlab/outputarea":"^4.0.0","@jupyterlab/rendermime":"^4.0.0","@jupyterlab/rendermime-extension":"^4.0.0","@jupyterlab/services":"^7.0.0","@jupyterlab/settingregistry":"^4.0.0","@jupyterlab/theme-dark-extension":"^4.0.2","@jupyterlab/theme-light-extension":"^4.0.2","@jupyterlab/translation":"^4.0.0","@jupyterlab/ui-components":"^4.0.0","@jupyterlab/vega5-extension":"^4.0.0","@lumino/algorithm":"^2.0.0","@lumino/commands":"^2.0.0","@lumino/coreutils":"^2.0.0","@lumino/datagrid":"^2.1.2","@lumino/disposable":"^2.0.0","@lumino/domutils":"^2.0.0","@lumino/dragdrop":"^2.0.0","@lumino/messaging":"^2.0.0","@lumino/properties":"^2.0.0","@lumino/signaling":"^2.0.0","@lumino/virtualdom":"^2.0.0","@lumino/widgets":"^2.0.0","react":"^18.2.0","react-dom":"^18.2.0","style-mod":"^4.0.3","util":"^0.12.5"},"devDependencies":{"@jupyterlab/builder":"^4.0.0","@types/node":"~18.8.3","css-loader":"^6.7.2","fs-extra":"^9.1.0","glob":"~7.1.6","npm-run-all":"^4.1.5","p-limit":"^2.2.2","rimraf":"^3.0.2","style-loader":"~3.3.1","tsc-watch":"^6.0.0","typescript":"~5.0.2","watch":"^1.0.2","webpack":"^5.24.1","webpack-bundle-analyzer":"^4.4.0","webpack-cli":"^4.5.0","webpack-merge":"^5.7.3","whatwg-fetch":"^3.0.0"},"scripts":{"build":"npm run build:lib && webpack --mode=development","build:lib":"tsc","build:prod":"npm run build:lib && webpack --mode=production","clean":"jlpm run clean:lib && jlpm run clean:asset && rimraf build","clean:lib":"rimraf lib tsconfig.tsbuildinfo","clean:asset":"rimraf ../../share/jupyter/voila/schemas ../../share/jupyter/voila/themes ../../share/jupyter/voila/style.js","test":"echo \\"Error: no test specified\\" && exit 1","watch":"tsc-watch --onSuccess \\"webpack --mode=development\\"","watch:lib":"tsc -w","watch:bundle":"webpack --watch --mode=development"}}')}}]);