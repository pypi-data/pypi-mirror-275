import{k as m}from"./kind-of-l3izQsJJ.js";import{e as k}from"./extend-shallow-DA8A8LGH.js";var S=m,x=k,E=function(t,e){typeof e=="function"&&(e={parse:e});var c=w(t),j={section_delimiter:"---",parse:O},l=x({},j,e),g=l.section_delimiter,v=c.content.split(/\r?\n/),r=null,o=p(),n=[],i=[];function y(h){c.content=h,r=[],n=[]}function d(h){i.length&&(o.key=B(i[0],g),o.content=h,l.parse(o,r),r.push(o),o=p(),n=[],i=[])}for(var f=0;f<v.length;f++){var u=v[f],a=i.length,s=u.trim();if(b(s,g)){if(s.length===3&&f!==0){if(a===0||a===2){n.push(u);continue}i.push(s),o.data=n.join(`
`),n=[];continue}r===null&&y(n.join(`
`)),a===2&&d(n.join(`
`)),i.push(s);continue}n.push(u)}return r===null?y(n.join(`
`)):d(n.join(`
`)),c.sections=r,c};function b(t,e){return!(t.slice(0,e.length)!==e||t.charAt(e.length+1)===e.slice(-1))}function w(t){if(S(t)!=="object"&&(t={content:t}),typeof t.content!="string"&&!_(t.content))throw new TypeError("expected a buffer or string");return t.content=t.content.toString(),t.sections=[],t}function B(t,e){return t?t.slice(e.length).trim():""}function p(){return{key:"",data:"",content:""}}function O(t){return t}function _(t){return t&&t.constructor&&typeof t.constructor.isBuffer=="function"?t.constructor.isBuffer(t):!1}export{E as s};
