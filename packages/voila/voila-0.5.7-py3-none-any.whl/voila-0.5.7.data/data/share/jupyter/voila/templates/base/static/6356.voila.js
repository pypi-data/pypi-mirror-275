"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[6356,8736],{38736:(t,e,r)=>{r.r(e),r.d(e,{MAJOR_VERSION:()=>u,MINOR_VERSION:()=>i,isCode:()=>c,isDisplayData:()=>l,isDisplayUpdate:()=>_,isError:()=>f,isExecuteResult:()=>s,isMarkdown:()=>p,isRaw:()=>o,isStream:()=>y,validateMimeValue:()=>a});var n=r(11296);const u=4,i=4;function a(t,e){const r="application/json"===t||/^application\/.+\+json$/.test(t),u=t=>"[object String]"===Object.prototype.toString.call(t);if(Array.isArray(e)){if(r)return!1;let t=!0;return e.forEach((e=>{u(e)||(t=!1)})),t}return u(e)?!r:!!r&&n.JSONExt.isObject(e)}function o(t){return"raw"===t.cell_type}function p(t){return"markdown"===t.cell_type}function c(t){return"code"===t.cell_type}function s(t){return"execute_result"===t.output_type}function l(t){return"display_data"===t.output_type}function _(t){return"update_display_data"===t.output_type}function y(t){return"stream"===t.output_type}function f(t){return"error"===t.output_type}}}]);