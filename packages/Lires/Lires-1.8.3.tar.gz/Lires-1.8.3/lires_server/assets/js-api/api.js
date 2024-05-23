(()=>{"use strict";var e={d:(t,a)=>{for(var s in a)e.o(a,s)&&!e.o(t,s)&&Object.defineProperty(t,s,{enumerable:!0,get:a[s]})},o:(e,t)=>Object.prototype.hasOwnProperty.call(e,t),r:e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}},t={};e.r(t),e.d(t,{HTTPPathResolver:()=>r,ServerConn:()=>n,default:()=>i});var a=function e(t){function a(e,t){return e>>>t|e<<32-t}for(var s,r,n=Math.pow,i=n(2,32),o="length",h="",c=[],u=8*t[o],d=e.h=e.h||[],p=e.k=e.k||[],l=p[o],f={},y=2;l<64;y++)if(!f[y]){for(s=0;s<313;s+=y)f[s]=y;d[l]=n(y,.5)*i|0,p[l++]=n(y,1/3)*i|0}for(t+="";t[o]%64-56;)t+="\0";for(s=0;s<t[o];s++){if((r=t.charCodeAt(s))>>8)throw new Error("ASCII check failed");c[s>>2]|=r<<(3-s)%4*8}for(c[c[o]]=u/i|0,c[c[o]]=u,r=0;r<c[o];){var m=c.slice(r,r+=16),w=d;for(d=d.slice(0,8),s=0;s<64;s++){var g=m[s-15],b=m[s-2],_=d[0],$=d[4],U=d[7]+(a($,6)^a($,11)^a($,25))+($&d[5]^~$&d[6])+p[s]+(m[s]=s<16?m[s]:m[s-16]+(a(g,7)^a(g,18)^g>>>3)+m[s-7]+(a(b,17)^a(b,19)^b>>>10)|0);(d=[U+((a(_,2)^a(_,13)^a(_,22))+(_&d[1]^_&d[2]^d[1]&d[2]))|0].concat(d))[4]=d[4]+U|0}for(s=0;s<8;s++)d[s]=d[s]+w[s]|0}for(s=0;s<8;s++)for(r=3;r+1;r--){var D=d[s]>>8*r&255;h+=(D<16?0:"")+D.toString(16)}return h};const s=class{constructor({baseUrlGetter:e=(()=>""),tokenGetter:t=(()=>""),sessionIDGetter:a=(()=>"")}){this._baseUrlGetter=e,this._tokenGetter=t,this._sessionIDGetter=a}get baseUrl(){return this._baseUrlGetter()}get token(){return this._tokenGetter()}get sessionID(){return this._sessionIDGetter()}async get(e,t={}){const a=new URL(`${this._baseUrlGetter()}${e}`);return Object.keys(t).forEach((e=>a.searchParams.append(e,t[e]))),await this._fetch(a.toString(),{method:"GET"})}async post(e,t={}){const a=new FormData;for(const e in t){let s=t[e];s instanceof Array&&(s=JSON.stringify(s)),a.append(e,s)}return await this._fetch(`${this._baseUrlGetter()}${e}`,{method:"POST",body:a})}async put(e,t){const a=new FormData;return a.append("key",this._tokenGetter()),a.append("session_id",this._sessionIDGetter()),a.append("file",t),await this._fetch(`${this._baseUrlGetter()}${e}`,{method:"PUT",body:a})}async delete(e,t={}){const a=new FormData;for(const e in t){let s=t[e];s instanceof Array&&(s=JSON.stringify(s)),a.append(e,s)}return a.append("key",this._tokenGetter()),a.append("session_id",this._sessionIDGetter()),await this._fetch(`${this._baseUrlGetter()}${e}`,{method:"DELETE",body:a})}async _fetch(e,t){if(void 0===t&&(t={}),void 0===t.headers?t.headers=new Headers:(t.headers,t.headers=new Headers(t.headers)),t.headers.append("Authorization",`Bearer ${this._tokenGetter()}`),"GET"===t?.method){const t=new URL(e);t.searchParams.append("session_id",this._sessionIDGetter()),e=t.toString()}else if("POST"===t?.method||"PUT"===t?.method||"DELETE"===t?.method)if("string"==typeof t.body)t.body=JSON.stringify({session_id:this._sessionIDGetter(),...JSON.parse(t.body)});else{if(!(t.body instanceof FormData))throw new Error("Not implemented body type");t.body.has("session_id")||t.body.append("session_id",this._sessionIDGetter())}const a=await fetch(e,t);if(!a.ok)throw new Error(`Request failed with status ${a.status}`);return a}};class r{baseURLGetter;tokenGetter;constructor(e,t=(()=>"")){this.baseURLGetter=e,this.tokenGetter=t}get baseURL(){return this.baseURLGetter()}get token(){return this.tokenGetter()}doc(e,t){return`${this.baseURL}/doc/${e}?_u=${t}`}docDry=(e,t)=>this.doc(e,t).replace("/doc/","/doc-dry/");docText=(e,t)=>this.doc(e,t).replace("/doc/","/doc-text/");databaseDownload(e=!1){return`${this.baseURL}/api/database/download?data=${e}&key=${this.token}`}miscFile(e,t){const a=encodeURIComponent(t);return`${this.baseURL}/misc/${e}?fname=${a}`}userAvatar(e,t={size:128,t:-1}){let a;return a=null===t.t?"":t.t<0?`&t=${Date.now()}`:`&t=${t.t}`,`${this.baseURL}/user-avatar/${e}?size=${t.size}${a}`}}class n{constructor(e,t,a=null){if(null===a){const e=Math.random().toString(36).substring(2);a=()=>e}this.fetcher=new s({baseUrlGetter:e,tokenGetter:t,sessionIDGetter:a}),this.resolve=new r(e,t)}get baseURL(){return this.fetcher.baseUrl}async authorize(){return await this.fetcher.post("/api/auth").then((e=>e.json()))}async status(){return await this.fetcher.get("/api/status").then((e=>e.json()))}async reqAllKeys(){return await this.fetcher.get("/api/database/keys").then((e=>e.json()))}async reqAllTags(){return await this.fetcher.get("/api/database/tags").then((e=>e.json()))}async reqDatabaseFeatureTSNE(e="doc_feature",t=3,a=10){return await this.fetcher.get(`/api/datafeat/tsne/${e}`,{n_component:t.toString(),perplexity:a.toString()}).then((e=>e.json()))}async reqDatabaseUsage(){return await this.fetcher.get("/api/database/usage").then((e=>e.json()))}async reqDatapointSummary(e){return await this.fetcher.get(`/api/datainfo/${e}`).then((e=>e.json()))}async reqDatapointSummaries(e){return await this.fetcher.post("/api/datainfo-list",{uids:JSON.stringify(e)}).then((e=>e.json()))}async deleteDatapoint(e){return await this.fetcher.post("/api/dataman/delete",{uuid:e}).then((()=>!0))}async updateDatapoint(e,{bibtex:t=null,tags:a=null,url:s=null}){if(!e&&(null===t||null===a||null===s))throw new Error("uid is null, other fields should be complete");const r={};return null!==e&&(r.uuid=e),null!==t&&(r.bibtex=t),null!==a&&(r.tags=JSON.stringify(a)),null!==s&&(r.url=s),await this.fetcher.post("/api/dataman/update",r).then((e=>e.json()))}async reqDatapointAbstract(e){return await this.fetcher.get(`/api/datainfo-supp/abstract/${e}`).then((e=>e.text()))}async updateDatapointAbstract(e,t){return await this.fetcher.post(`/api/datainfo-supp/abstract-update/${e}`,{content:t}).then((e=>!0))}async reqDatapointNote(e){return await this.fetcher.get(`/api/datainfo-supp/note/${e}`).then((e=>e.text()))}async updateDatapointNote(e,t){return await this.fetcher.post(`/api/datainfo-supp/note-update/${e}`,{content:t}).then((e=>!0))}async query({tags:e=[],searchBy:t="title",searchContent:a="",maxResults:s=9999}={}){return await this.fetcher.post("/api/filter/basic",{tags:e,search_by:t,search_content:a,top_k:s}).then((e=>e.json()))}async featurizeText(e,t=!1){return await this.fetcher.post("/api/iserver/textFeature",{text:e,require_cache:t}).then((e=>e.json()))}reqAISummary(e,t,a=(()=>{}),s=!0,r="DEFAULT"){this.fetcher.post("/api/summary",{force:s,uuid:e,model:r}).then((e=>{if(!e.ok)throw t("(Error: "+e.status+")"),new Error("HTTP error "+e.status);const s=e.body.getReader(),r=({value:e,done:n})=>{if(n)return void a();let i=(new TextDecoder).decode(e);return t(i),s.read().then(r)};return s.read().then(r)}))}async reqMiscFileList(e){return await this.fetcher.get(`/api/misc-list/${e}`).then((e=>e.json()))}async deleteMiscFile(e,t){return await this.fetcher.delete(`/misc/${e}`,{fname:t}).then((()=>!0))}async renameMiscFile(e,t,a){return await this.fetcher.post(`/misc/${e}`,{fname:t,dst_fname:a}).then((()=>!0))}async uploadMiscFiles(e,t){return(await Promise.all(t.map((t=>new Promise(((a,s)=>{this.fetcher.put(`/misc/${e}`,t).then((e=>e.json())).then(a).catch(s)})))))).map((e=>e.file_name))}async uploadDocument(e,t){return await this.fetcher.put(`/doc/${e}`,t).then((e=>e.json()))}async deleteDocument(e){return await this.fetcher.delete(`/doc/${e}`).then((e=>e.json()))}async updateTagAll(e,t){return await this.fetcher.post("/api/database/tag-rename",{oldTag:e,newTag:t}).then((()=>!0))}async deleteTagAll(e){return await this.fetcher.post("/api/database/tag-delete",{tag:e}).then((()=>!0))}async reqUserInfo(e){return await this.fetcher.post(`/api/user/info/${e}`).then((e=>e.json()))}async updateUserNickname(e){return await this.fetcher.post("/api/user/info-update",{name:e}).then((e=>e.json()))}async updateUserPassword(e){return await this.fetcher.post("/api/user/info-update",{password:a(e)}).then((e=>e.json()))}async reqUserList(){return await this.fetcher.post("/api/user/list",{}).then((e=>e.json()))}async uploadUserAvatar(e,t){return await this.fetcher.put(`/user-avatar/${e}`,t).then((e=>e.json()))}async updateUserAccess(e,t,a,s){const r={};return r.username=e,null!==t&&(r.is_admin=t.toString()),null!==a&&(r.mandatory_tags=JSON.stringify(a)),null!==s&&(r.max_storage=s),await this.fetcher.post("/api/userman/modify",r).then((e=>e.json()))}async registerUser(e,t,s,r){return await this.fetcher.post("/api/userman/register",{invitation_code:e,username:t,password:a(s),name:r}).then((e=>e.json()))}async createUser(e,t,s,r,n,i){return await this.fetcher.post("/api/userman/create",{username:e,name:t,password:a(s),is_admin:r.toString(),mandatory_tags:JSON.stringify(n),max_storage:i}).then((e=>e.json()))}async deleteUser(e){return await this.fetcher.post("/api/userman/delete",{username:e}).then((()=>!0))}async reqFeedList({maxResults:e=10,category:t="",timeBefore:a=-1,timeAfter:s=-1}){return console.log("reqFeedList",e,t,a,s),await this.fetcher.post("/api/feed/query",{max_results:e,category:t,time_before:a,time_after:s}).then((e=>e.json()))}async reqFeedCategories(){return await this.fetcher.get("/api/feed/categories").then((e=>e.json()))}async changelog(){return await this.fetcher.get("/api/info/changelog").then((e=>e.json()))}}const i=n;exports.HTTPPathResolver=t.HTTPPathResolver,exports.ServerConn=t.ServerConn,exports.default=t.default,Object.defineProperty(exports,"__esModule",{value:!0})})();