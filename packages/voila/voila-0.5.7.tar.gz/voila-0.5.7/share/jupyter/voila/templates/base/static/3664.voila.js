/*! For license information please see 3664.voila.js.LICENSE.txt */
"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[3664],{31284:(t,e,n)=>{n.r(e),n.d(e,{ConflatableMessage:()=>l,Message:()=>a,MessageLoop:()=>f});var r,i=n(61136),o=function(){function t(t){this._root=new r.LeafNode,this.cmp=t}return Object.defineProperty(t.prototype,"isEmpty",{get:function(){return 0===this._root.size},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"size",{get:function(){return this._root.size},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"first",{get:function(){var t=r.firstLeaf(this._root);return t.size>0?t.items[0]:void 0},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"last",{get:function(){var t=r.lastLeaf(this._root);return t.size>0?t.items[t.size-1]:void 0},enumerable:!0,configurable:!0}),t.prototype.iter=function(){return r.iterItems(this._root)},t.prototype.retro=function(){return r.retroItems(this._root)},t.prototype.slice=function(t,e){return r.sliceItems(this._root,t,e)},t.prototype.retroSlice=function(t,e){return r.retroSliceItems(this._root,t,e)},t.prototype.at=function(t){return r.itemAt(this._root,t)},t.prototype.has=function(t,e){return r.hasItem(this._root,t,e)},t.prototype.indexOf=function(t,e){return r.indexOf(this._root,t,e)},t.prototype.get=function(t,e){return r.getItem(this._root,t,e)},t.prototype.assign=function(t){this.clear(),this.update(t)},t.prototype.insert=function(t){var e=r.insertItem(this._root,t,this.cmp);return this._root=r.maybeSplitRoot(this._root),e},t.prototype.update=function(t){var e=this;(0,i.each)(t,(function(t){e.insert(t)}))},t.prototype.delete=function(t,e){var n=r.deleteItem(this._root,t,e);return this._root=r.maybeExtractRoot(this._root),n},t.prototype.remove=function(t){var e=r.removeItem(this._root,t);return this._root=r.maybeExtractRoot(this._root),e},t.prototype.clear=function(){r.clear(this._root),this._root=new r.LeafNode},t}();!function(t){t.from=function(e,n){var r=new t(n);return r.assign(e),r}}(o||(o={})),function(t){var e=function(){function t(){this.items=[],this.sizes=[],this.children=[]}return Object.defineProperty(t.prototype,"type",{get:function(){return 0},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"size",{get:function(){return this.sizes[this.sizes.length-1]},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"width",{get:function(){return this.children.length},enumerable:!0,configurable:!0}),t}();t.BranchNode=e;var n=function(){function t(){this.next=null,this.prev=null,this.items=[]}return Object.defineProperty(t.prototype,"type",{get:function(){return 1},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"size",{get:function(){return this.items.length},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"width",{get:function(){return this.items.length},enumerable:!0,configurable:!0}),t}();function r(t){for(;0===t.type;)t=t.children[0];return t}function o(t){for(;0===t.type;)t=t.children[t.children.length-1];return t}function s(t){0===t.type?((0,i.each)(t.children,s),t.children.length=0,t.sizes.length=0,t.items.length=0):(t.items.length=0,t.next=null,t.prev=null)}t.LeafNode=n,t.firstLeaf=r,t.lastLeaf=o,t.iterItems=function(t){var e=r(t);return new h(e,0,-1)},t.retroItems=function(t){var e=o(t);return new a(e,e.size-1,-1)},t.sliceItems=function(t,e,n){e=void 0===e?0:e<0?Math.max(0,e+t.size):Math.min(e,t.size),n=void 0===n?t.size:n<0?Math.max(0,n+t.size):Math.min(n,t.size);var r=Math.max(0,n-e);if(0===r)return(0,i.empty)();for(;0===t.type;){var o=l(t.sizes,e);o>0&&(e-=t.sizes[o-1]),t=t.children[o]}return new h(t,e,r)},t.retroSliceItems=function(t,e,n){e=void 0===e?t.size-1:e<0?Math.max(-1,e+t.size):Math.min(e,t.size-1),n=void 0===n?-1:n<0?Math.max(-1,n+t.size):Math.min(n,t.size-1);var r=Math.max(0,e-n);if(0===r)return(0,i.empty)();for(;0===t.type;){var o=l(t.sizes,e);o>0&&(e-=t.sizes[o-1]),t=t.children[o]}return new a(t,e,r)},t.itemAt=function(t,e){if(e<0&&(e+=t.size),!(e<0||e>=t.size)){for(;0===t.type;){var n=l(t.sizes,e);n>0&&(e-=t.sizes[n-1]),t=t.children[n]}return t.items[e]}},t.hasItem=function(t,e,n){for(;0===t.type;){var r=c(t.items,e,n);t=t.children[r]}return p(t.items,e,n)>=0},t.indexOf=function(t,e,n){for(var r=0;0===t.type;){var i=c(t.items,e,n);i>0&&(r+=t.sizes[i-1]),t=t.children[i]}var o=p(t.items,e,n);return o>=0?r+o:-r+o},t.getItem=function(t,e,n){for(;0===t.type;){var r=c(t.items,e,n);t=t.children[r]}var i=p(t.items,e,n);return i>=0?t.items[i]:void 0},t.insertItem=function t(e,n,r){if(1===e.type){var o,s=p(e.items,n,r);return s>=0?(o=e.items[s],e.items[s]=n):(o=void 0,i.ArrayExt.insert(e.items,-s-1,n)),o}var f=c(e.items,n,r),h=e.children[f],a=h.size,l=t(h,n,r),_=h.size;if(e.items[f]=h.items[0],a===_)return l;if(h.width>u){var y=m(h);i.ArrayExt.insert(e.children,f+1,y),i.ArrayExt.insert(e.items,f+1,y.items[0])}return d(e,f),l},t.deleteItem=function t(e,n,r){if(1===e.type){var o=p(e.items,n,r);if(o<0)return;return i.ArrayExt.removeAt(e.items,o)}var s=c(e.items,n,r),u=e.children[s],h=u.size,a=t(u,n,r);return h===u.size||(e.items[s]=u.items[0],u.width<f&&(s=_(e,s)),d(e,s)),a},t.removeItem=function t(e,n){if(n<0&&(n+=e.size),!(n<0||n>=e.size)){if(1===e.type)return i.ArrayExt.removeAt(e.items,n);var r=l(e.sizes,n);r>0&&(n-=e.sizes[r]);var o=e.children[r],s=t(o,n);return e.items[r]=o.items[0],o.width<f&&(r=_(e,r)),d(e,r),s}},t.clear=s,t.maybeSplitRoot=function(t){if(t.width<=u)return t;var n=new e,r=m(t);return n.sizes[0]=t.size,n.sizes[1]=t.size+r.size,n.children[0]=t,n.children[1]=r,n.items[0]=t.items[0],n.items[1]=r.items[0],n},t.maybeExtractRoot=function(t){if(1===t.type)return t;if(t.children.length>1)return t;var e=t.children.pop();return s(t),e};var u=32,f=u>>1,h=function(){function t(t,e,n){this._node=t,this._index=e,this._count=n}return t.prototype.iter=function(){return this},t.prototype.clone=function(){return new t(this._node,this._index,this._count)},t.prototype.next=function(){if(null!==this._node&&0!==this._count)return this._index>=this._node.size?(this._node=this._node.next,this._index=0,this.next()):(this._count>0&&this._count--,this._node.items[this._index++])},t}(),a=function(){function t(t,e,n){this._node=t,this._index=e,this._count=n}return t.prototype.iter=function(){return this},t.prototype.clone=function(){return new t(this._node,this._index,this._count)},t.prototype.next=function(){if(null!==this._node&&0!==this._count)return this._index>=this._node.size&&(this._index=this._node.size-1),this._index<0?(this._node=this._node.prev,this._index=this._node?this._node.size-1:-1,this.next()):(this._count>0&&this._count--,this._node.items[this._index--])},t}();function l(t,e){for(var n=t.length,r=0;r<n;++r)if(t[r]>e)return r;return n-1}function c(t,e,n){for(var r=t.length,i=1;i<r;++i)if(n(t[i],e)>0)return i-1;return r-1}function p(t,e,n){for(var r=t.length,i=0;i<r;++i){var o=n(t[i],e);if(0===o)return i;if(o>0)return-i-1}return-r-1}function d(t,e){for(var n=t.sizes,r=t.children,i=e>0?n[e-1]:0,o=r.length;e<o;++e)i=n[e]=i+r[e].size;n.length=r.length}function m(t){if(1===t.type){for(var r=new n,i=t.items,o=r.items,s=f,u=i.length;s<u;++s)o.push(i[s]);return i.length=f,t.next&&(t.next.prev=r),r.next=t.next,r.prev=t,t.next=r,r}var h=new e,a=t.children,l=h.children;for(s=f,u=a.length;s<u;++s)l.push(a[s]);a.length=f;var c=t.items,p=h.items;for(s=f,u=c.length;s<u;++s)p.push(c[s]);return c.length=f,d(t,f),d(h,0),h}function _(t,e){var n,r,o,u,h,a,l=t.children[e],c=0===e?t.children[e+1]:t.children[e-1],p=0===e,m=1===l.type,_=c.width>f;if(m&&_&&p){var y=c;return(v=l).items.push(y.items.shift()),t.items[e+1]=y.items[0],e}if(m&&_&&!p)return y=c,(v=l).items.unshift(y.items.pop()),t.items[e]=v.items[0],e-1;if(m&&!_&&p){var v=l;return(n=(y=c).items).unshift.apply(n,v.items),i.ArrayExt.removeAt(t.children,e),i.ArrayExt.removeAt(t.items,e+1),v.prev&&(v.prev.next=y),y.prev=v.prev,s(v),e}if(m&&!_&&!p)return v=l,(r=(y=c).items).push.apply(r,v.items),i.ArrayExt.removeAt(t.children,e),i.ArrayExt.removeAt(t.items,e),v.next&&(v.next.prev=y),y.next=v.next,s(v),e-1;if(!m&&_&&p)return y=c,(v=l).children.push(y.children.shift()),v.items.push(y.items.shift()),t.items[e+1]=y.items[0],d(v,v.width-1),d(y,0),e;if(!m&&_&&!p)return y=c,(v=l).children.unshift(y.children.pop()),v.items.unshift(y.items.pop()),t.items[e]=v.items[0],d(v,0),d(y,y.width-1),e-1;if(!m&&!_&&p)return v=l,(o=(y=c).children).unshift.apply(o,v.children),(u=y.items).unshift.apply(u,v.items),i.ArrayExt.removeAt(t.children,e),i.ArrayExt.removeAt(t.items,e+1),d(y,0),v.children.length=0,s(v),e;if(!m&&!_&&!p)return v=l,(h=(y=c).children).push.apply(h,v.children),(a=y.items).push.apply(a,v.items),i.ArrayExt.removeAt(t.children,e),i.ArrayExt.removeAt(t.items,e),d(y,0),v.children.length=0,s(v),e-1;throw"unreachable"}}(r||(r={}));var s,u=function(){function t(){this._first=null,this._last=null,this._size=0}return Object.defineProperty(t.prototype,"isEmpty",{get:function(){return 0===this._size},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"size",{get:function(){return this._size},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"length",{get:function(){return this._size},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"first",{get:function(){return this._first?this._first.value:void 0},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"last",{get:function(){return this._last?this._last.value:void 0},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"firstNode",{get:function(){return this._first},enumerable:!0,configurable:!0}),Object.defineProperty(t.prototype,"lastNode",{get:function(){return this._last},enumerable:!0,configurable:!0}),t.prototype.iter=function(){return new t.ForwardValueIterator(this._first)},t.prototype.retro=function(){return new t.RetroValueIterator(this._last)},t.prototype.nodes=function(){return new t.ForwardNodeIterator(this._first)},t.prototype.retroNodes=function(){return new t.RetroNodeIterator(this._last)},t.prototype.assign=function(t){var e=this;this.clear(),(0,i.each)(t,(function(t){e.addLast(t)}))},t.prototype.push=function(t){this.addLast(t)},t.prototype.pop=function(){return this.removeLast()},t.prototype.shift=function(t){this.addFirst(t)},t.prototype.unshift=function(){return this.removeFirst()},t.prototype.addFirst=function(t){var e=new s.LinkedListNode(this,t);return this._first?(e.next=this._first,this._first.prev=e,this._first=e):(this._first=e,this._last=e),this._size++,e},t.prototype.addLast=function(t){var e=new s.LinkedListNode(this,t);return this._last?(e.prev=this._last,this._last.next=e,this._last=e):(this._first=e,this._last=e),this._size++,e},t.prototype.insertBefore=function(t,e){if(!e||e===this._first)return this.addFirst(t);if(!(e instanceof s.LinkedListNode)||e.list!==this)throw new Error("Reference node is not owned by the list.");var n=new s.LinkedListNode(this,t),r=e,i=r.prev;return n.next=r,n.prev=i,r.prev=n,i.next=n,this._size++,n},t.prototype.insertAfter=function(t,e){if(!e||e===this._last)return this.addLast(t);if(!(e instanceof s.LinkedListNode)||e.list!==this)throw new Error("Reference node is not owned by the list.");var n=new s.LinkedListNode(this,t),r=e,i=r.next;return n.next=i,n.prev=r,r.next=n,i.prev=n,this._size++,n},t.prototype.removeFirst=function(){var t=this._first;if(t)return t===this._last?(this._first=null,this._last=null):(this._first=t.next,this._first.prev=null),t.list=null,t.next=null,t.prev=null,this._size--,t.value},t.prototype.removeLast=function(){var t=this._last;if(t)return t===this._first?(this._first=null,this._last=null):(this._last=t.prev,this._last.next=null),t.list=null,t.next=null,t.prev=null,this._size--,t.value},t.prototype.removeNode=function(t){if(!(t instanceof s.LinkedListNode)||t.list!==this)throw new Error("Node is not owned by the list.");var e=t;e===this._first&&e===this._last?(this._first=null,this._last=null):e===this._first?(this._first=e.next,this._first.prev=null):e===this._last?(this._last=e.prev,this._last.next=null):(e.next.prev=e.prev,e.prev.next=e.next),e.list=null,e.next=null,e.prev=null,this._size--},t.prototype.clear=function(){for(var t=this._first;t;){var e=t.next;t.list=null,t.prev=null,t.next=null,t=e}this._first=null,this._last=null,this._size=0},t}();!function(t){t.from=function(e){var n=new t;return n.assign(e),n};var e=function(){function t(t){this._node=t}return t.prototype.iter=function(){return this},t.prototype.clone=function(){return new t(this._node)},t.prototype.next=function(){if(this._node){var t=this._node;return this._node=t.next,t.value}},t}();t.ForwardValueIterator=e;var n=function(){function t(t){this._node=t}return t.prototype.iter=function(){return this},t.prototype.clone=function(){return new t(this._node)},t.prototype.next=function(){if(this._node){var t=this._node;return this._node=t.prev,t.value}},t}();t.RetroValueIterator=n;var r=function(){function t(t){this._node=t}return t.prototype.iter=function(){return this},t.prototype.clone=function(){return new t(this._node)},t.prototype.next=function(){if(this._node){var t=this._node;return this._node=t.next,t}},t}();t.ForwardNodeIterator=r;var i=function(){function t(t){this._node=t}return t.prototype.iter=function(){return this},t.prototype.clone=function(){return new t(this._node)},t.prototype.next=function(){if(this._node){var t=this._node;return this._node=t.prev,t}},t}();t.RetroNodeIterator=i}(u||(u={})),function(t){t.LinkedListNode=function(t,e){this.list=null,this.next=null,this.prev=null,this.list=t,this.value=e}}(s||(s={}));var f,h=function(t,e){return h=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(t[n]=e[n])},h(t,e)},a=function(){function t(t){this.type=t}return Object.defineProperty(t.prototype,"isConflatable",{get:function(){return!1},enumerable:!0,configurable:!0}),t.prototype.conflate=function(t){return!1},t}(),l=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function n(){this.constructor=t}h(t,e),t.prototype=null===e?Object.create(e):(n.prototype=e.prototype,new n)}(e,t),Object.defineProperty(e.prototype,"isConflatable",{get:function(){return!0},enumerable:!0,configurable:!0}),e.prototype.conflate=function(t){return!0},e}(a);!function(t){function e(t,e){var n=r.get(t);if(n&&0!==n.length){var o=(0,i.every)((0,i.retro)(n),(function(n){return!n||function(t,e,n){var r=!0;try{r="function"==typeof t?t(e,n):t.messageHook(e,n)}catch(t){s(t)}return r}(n,t,e)}));o&&c(t,e)}else c(t,e)}t.sendMessage=e,t.postMessage=function(t,e){e.isConflatable&&(0,i.some)(n,(function(n){return n.handler===t&&!!n.msg&&n.msg.type===e.type&&!!n.msg.isConflatable&&n.msg.conflate(e)}))||function(t,e){n.addLast({handler:t,msg:e}),0===f&&(f=a(p))}(t,e)},t.installMessageHook=function(t,e){var n=r.get(t);n&&-1!==n.indexOf(e)||(n?n.push(e):r.set(t,[e]))},t.removeMessageHook=function(t,e){var n=r.get(t);if(n){var i=n.indexOf(e);-1!==i&&(n[i]=null,d(n))}},t.clearData=function(t){var e=r.get(t);e&&e.length>0&&(i.ArrayExt.fill(e,null),d(e)),(0,i.each)(n,(function(e){e.handler===t&&(e.handler=null,e.msg=null)}))},t.flush=function(){h||0===f||(l(f),h=!0,p(),h=!1)},t.getExceptionHandler=function(){return s},t.setExceptionHandler=function(t){var e=s;return s=t,e};var n=new u,r=new WeakMap,o=new Set,s=function(t){console.error(t)},f=0,h=!1,a="function"==typeof requestAnimationFrame?requestAnimationFrame:setImmediate,l="function"==typeof cancelAnimationFrame?cancelAnimationFrame:clearImmediate;function c(t,e){try{t.processMessage(e)}catch(t){s(t)}}function p(){if(f=0,!n.isEmpty){var t={handler:null,msg:null};for(n.addLast(t);;){var r=n.removeFirst();if(r===t)return;r.handler&&r.msg&&e(r.handler,r.msg)}}}function d(t){0===o.size&&a(m),o.add(t)}function m(){o.forEach(_),o.clear()}function _(t){i.ArrayExt.removeAllWhere(t,y)}function y(t){return null===t}}(f||(f={}))}}]);