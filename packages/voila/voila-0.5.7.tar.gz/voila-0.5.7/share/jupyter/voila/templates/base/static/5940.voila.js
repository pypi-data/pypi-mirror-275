"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[5940,8320],{8320:(__unused_webpack_module,__webpack_exports__,__webpack_require__)=>{__webpack_require__.r(__webpack_exports__),__webpack_require__.d(__webpack_exports__,{APPLICATION_JAVASCRIPT_MIMETYPE:()=>APPLICATION_JAVASCRIPT_MIMETYPE,ExperimentalRenderedJavascript:()=>ExperimentalRenderedJavascript,TEXT_JAVASCRIPT_MIMETYPE:()=>TEXT_JAVASCRIPT_MIMETYPE,default:()=>__WEBPACK_DEFAULT_EXPORT__,rendererFactory:()=>rendererFactory});var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(89220),_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0___default=__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__);const TEXT_JAVASCRIPT_MIMETYPE="text/javascript",APPLICATION_JAVASCRIPT_MIMETYPE="application/javascript";function evalInContext(code,element,document,window){return eval(code)}class ExperimentalRenderedJavascript extends _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__.RenderedJavaScript{render(e){const _=this.translator.load("jupyterlab"),r=()=>{try{const _=e.data[this.mimeType];return _&&evalInContext(_,this.node,document,window),Promise.resolve()}catch(e){return Promise.reject(e)}};if(!e.trusted){const e=document.createElement("pre");e.textContent=_.__("Are you sure that you want to run arbitrary Javascript within your JupyterLab session?");const t=document.createElement("button");return t.textContent=_.__("Run"),this.node.appendChild(e),this.node.appendChild(t),t.onclick=e=>{this.node.textContent="",r()},Promise.resolve()}return r()}}const rendererFactory={safe:!1,mimeTypes:[TEXT_JAVASCRIPT_MIMETYPE,APPLICATION_JAVASCRIPT_MIMETYPE],createRenderer:e=>new ExperimentalRenderedJavascript(e)},extension={id:"@jupyterlab/javascript-extension:factory",description:"Adds renderer for JavaScript content.",rendererFactory,rank:0,dataType:"string"},__WEBPACK_DEFAULT_EXPORT__=extension}}]);