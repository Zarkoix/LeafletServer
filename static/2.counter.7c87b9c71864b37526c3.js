webpackJsonp([2],{91:function(e,t,n){var r=n(48),o=n(155),i=n(154),c=n(47),u=n(95),s=n(167),a={},f={},t=e.exports=function(e,t,n,l,d){var v,h,_,p,m=d?function(){return e}:s(e),y=r(n,l,t?2:1),b=0;if("function"!=typeof m)throw TypeError(e+" is not iterable!");if(i(m)){for(v=u(e.length);v>b;b++)if(p=t?y(c(h=e[b])[0],h[1]):y(e[b]),p===a||p===f)return p}else for(_=m.call(e);!(h=_.next()).done;)if(p=o(_,y,h.value,t),p===a||p===f)return p};t.BREAK=a,t.RETURN=f},107:function(e,t){e.exports=function(e,t,n,r){if(!(e instanceof t)||void 0!==r&&r in e)throw TypeError(n+": incorrect invocation!");return e}},112:function(e,t,n){var r=n(49);e.exports=function(e,t,n){for(var o in t)n&&e[o]?e[o]=t[o]:r(e,o,t[o]);return e}},148:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}t.__esModule=!0;var o=n(105),i=r(o);t.default=function(e,t,n){return t in e?(0,i.default)(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}},159:function(e,t,n){"use strict";var r=n(29),o=n(24),i=n(35),c=n(37),u=n(28)("species");e.exports=function(e){var t="function"==typeof o[e]?o[e]:r[e];c&&t&&!t[u]&&i.f(t,u,{configurable:!0,get:function(){return this}})}},231:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}function o(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:1;return{type:l,payload:e}}function i(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:_,t=arguments[1],n=h[t.type];return n?n(e,t):e}Object.defineProperty(t,"__esModule",{value:!0}),t.actions=t.doubleAsync=t.COUNTER_DOUBLE_ASYNC=t.COUNTER_INCREMENT=void 0;var c,u=n(148),s=r(u),a=n(411),f=r(a);t.increment=o,t.default=i;var l=t.COUNTER_INCREMENT="COUNTER_INCREMENT",d=t.COUNTER_DOUBLE_ASYNC="COUNTER_DOUBLE_ASYNC",v=t.doubleAsync=function(){return function(e,t){return new f.default(function(n){setTimeout(function(){e({type:d,payload:t().counter}),n()},200)})}},h=(t.actions={increment:o,doubleAsync:v},c={},(0,s.default)(c,l,function(e,t){return e+t.payload}),(0,s.default)(c,d,function(e,t){return 2*e}),c),_=0},381:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}Object.defineProperty(t,"__esModule",{value:!0}),t.Counter=void 0;var o=n(1),i=r(o),c=n(3),u=r(c),s=t.Counter=function(e){return i.default.createElement("div",{style:{margin:"0 auto"}},i.default.createElement("h2",null,"Counter: ",e.counter),i.default.createElement("button",{className:"btn btn-default",onClick:e.increment},"Increment")," ",i.default.createElement("button",{className:"btn btn-default",onClick:e.doubleAsync},"Double (Async)"))};s.propTypes={counter:u.default.number.isRequired,doubleAsync:u.default.func.isRequired,increment:u.default.func.isRequired},t.default=s},382:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}Object.defineProperty(t,"__esModule",{value:!0});var o=n(53),i=n(231),c=n(381),u=r(c),s={increment:function(){return(0,i.increment)(1)},doubleAsync:i.doubleAsync},a=function(e){return{counter:e.counter}};t.default=(0,o.connect)(a,s)(u.default)},411:function(e,t,n){e.exports={default:n(424),__esModule:!0}},424:function(e,t,n){n(168),n(114),n(169),n(459),e.exports=n(24).Promise},442:function(e,t,n){var r=n(29),o=n(162).set,i=r.MutationObserver||r.WebKitMutationObserver,c=r.process,u=r.Promise,s="process"==n(90)(c);e.exports=function(){var e,t,n,a=function(){var r,o;for(s&&(r=c.domain)&&r.exit();e;){o=e.fn,e=e.next;try{o()}catch(r){throw e?n():t=void 0,r}}t=void 0,r&&r.enter()};if(s)n=function(){c.nextTick(a)};else if(i){var f=!0,l=document.createTextNode("");new i(a).observe(l,{characterData:!0}),n=function(){l.data=f=!f}}else if(u&&u.resolve){var d=u.resolve();n=function(){d.then(a)}}else n=function(){o.call(r,a)};return function(r){var o={fn:r,next:void 0};t&&(t.next=o),e||(e=o,n()),t=o}}},447:function(e,t,n){var r=n(47),o=n(149),i=n(28)("species");e.exports=function(e,t){var n,c=r(e).constructor;return void 0===c||void 0==(n=r(c)[i])?t:o(n)}},459:function(e,t,n){"use strict";var r,o,i,c=n(109),u=n(29),s=n(48),a=n(150),f=n(34),l=n(55),d=n(149),v=n(107),h=n(91),_=n(447),p=n(162).set,m=n(442)(),y="Promise",b=u.TypeError,E=u.process,N=u[y],E=u.process,w="process"==a(E),C=function(){},R=!!function(){try{var e=N.resolve(1),t=(e.constructor={})[n(28)("species")]=function(e){e(C,C)};return(w||"function"==typeof PromiseRejectionEvent)&&e.then(C)instanceof t}catch(e){}}(),T=function(e,t){return e===t||e===N&&t===i},j=function(e){var t;return!(!l(e)||"function"!=typeof(t=e.then))&&t},x=function(e){return T(N,e)?new M(e):new o(e)},M=o=function(e){var t,n;this.promise=new e(function(e,r){if(void 0!==t||void 0!==n)throw b("Bad Promise constructor");t=e,n=r}),this.resolve=d(t),this.reject=d(n)},O=function(e){try{e()}catch(e){return{error:e}}},A=function(e,t){if(!e._n){e._n=!0;var n=e._c;m(function(){for(var r=e._v,o=1==e._s,i=0,c=function(t){var n,i,c=o?t.ok:t.fail,u=t.resolve,s=t.reject,a=t.domain;try{c?(o||(2==e._h&&g(e),e._h=1),c===!0?n=r:(a&&a.enter(),n=c(r),a&&a.exit()),n===t.promise?s(b("Promise-chain cycle")):(i=j(n))?i.call(n,u,s):u(n)):s(r)}catch(e){s(e)}};n.length>i;)c(n[i++]);e._c=[],e._n=!1,t&&!e._h&&P(e)})}},P=function(e){p.call(u,function(){var t,n,r,o=e._v;if(U(e)&&(t=O(function(){w?E.emit("unhandledRejection",o,e):(n=u.onunhandledrejection)?n({promise:e,reason:o}):(r=u.console)&&r.error&&r.error("Unhandled promise rejection",o)}),e._h=w||U(e)?2:1),e._a=void 0,t)throw t.error})},U=function(e){if(1==e._h)return!1;for(var t,n=e._a||e._c,r=0;n.length>r;)if(t=n[r++],t.fail||!U(t.promise))return!1;return!0},g=function(e){p.call(u,function(){var t;w?E.emit("rejectionHandled",e):(t=u.onrejectionhandled)&&t({promise:e,reason:e._v})})},k=function(e){var t=this;t._d||(t._d=!0,t=t._w||t,t._v=e,t._s=2,t._a||(t._a=t._c.slice()),A(t,!0))},S=function(e){var t,n=this;if(!n._d){n._d=!0,n=n._w||n;try{if(n===e)throw b("Promise can't be resolved itself");(t=j(e))?m(function(){var r={_w:n,_d:!1};try{t.call(e,s(S,r,1),s(k,r,1))}catch(e){k.call(r,e)}}):(n._v=e,n._s=1,A(n,!1))}catch(e){k.call({_w:n,_d:!1},e)}}};R||(N=function(e){v(this,N,y,"_h"),d(e),r.call(this);try{e(s(S,this,1),s(k,this,1))}catch(e){k.call(this,e)}},r=function(e){this._c=[],this._a=void 0,this._s=0,this._d=!1,this._v=void 0,this._h=0,this._n=!1},r.prototype=n(112)(N.prototype,{then:function(e,t){var n=x(_(this,N));return n.ok="function"!=typeof e||e,n.fail="function"==typeof t&&t,n.domain=w?E.domain:void 0,this._c.push(n),this._a&&this._a.push(n),this._s&&A(this,!1),n.promise},catch:function(e){return this.then(void 0,e)}}),M=function(){var e=new r;this.promise=e,this.resolve=s(S,e,1),this.reject=s(k,e,1)}),f(f.G+f.W+f.F*!R,{Promise:N}),n(94)(N,y),n(159)(y),i=n(24)[y],f(f.S+f.F*!R,y,{reject:function(e){var t=x(this),n=t.reject;return n(e),t.promise}}),f(f.S+f.F*(c||!R),y,{resolve:function(e){if(e instanceof N&&T(e.constructor,this))return e;var t=x(this),n=t.resolve;return n(e),t.promise}}),f(f.S+f.F*!(R&&n(240)(function(e){N.all(e).catch(C)})),y,{all:function(e){var t=this,n=x(t),r=n.resolve,o=n.reject,i=O(function(){var n=[],i=0,c=1;h(e,!1,function(e){var u=i++,s=!1;n.push(void 0),c++,t.resolve(e).then(function(e){s||(s=!0,n[u]=e,--c||r(n))},o)}),--c||r(n)});return i&&o(i.error),n.promise},race:function(e){var t=this,n=x(t),r=n.reject,o=O(function(){h(e,!1,function(e){t.resolve(e).then(n.resolve,r)})});return o&&r(o.error),n.promise}})}});