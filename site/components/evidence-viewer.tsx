"use client";
import React, { useEffect, useState } from "react";
import { Download, ExternalLink, FileText, LoaderCircle } from "lucide-react";
import { Sheet, SheetContent, SheetDescription, SheetHeader, SheetTitle } from "@/components/ui/sheet";
import { Table, TableBody, TableRow, TableCell, TableHead, TableHeader } from "@/components/ui/table";

export function EvidenceViewer({path,onClose}:{path:string|null;onClose:()=>void}) {
 const [text,setText]=useState("");const [error,setError]=useState("");
 useEffect(()=>{setText("");setError("");if(!path)return;const c=new AbortController();fetch(`/evidence/${path}`,{signal:c.signal}).then(r=>{if(!r.ok)throw Error("This report could not be loaded.");return r.text()}).then(setText).catch(e=>{if(e.name!=="AbortError")setError(e.message)});return()=>c.abort()},[path]);
 return <Sheet open={!!path} onOpenChange={open=>{if(!open)onClose()}}><SheetContent className="evidence-sheet"><SheetHeader><SheetTitle className="flex gap-3 items-center"><FileText size={20}/>{path?.split('/').at(-1)}</SheetTitle><SheetDescription>Original publication report · Frozen experiment 09 Sep 2026</SheetDescription></SheetHeader><div className="px-6 pb-3 border-b border-border"><a className="action small" href={`/evidence/${path}`} download><Download size={15}/>Download source</a></div><div className="report-content">{error?<p role="alert">{error}</p>:!text?<p className="flex gap-2"><LoaderCircle className="animate-spin"/>Loading report…</p>:<Markdown text={text} path={path??""}/>}</div></SheetContent></Sheet>;
}
function safeLink(href:string,path:string) {if(/^https?:\/\//i.test(href))return href;if(href.startsWith('#'))return href;const resolved=new URL(href,`https://evidence.local/${path}`);return `/evidence${resolved.pathname}${resolved.hash}`;}
function inline(text:string,path:string):React.ReactNode[] {return text.split(/(\*\*[^*]+\*\*|`[^`]+`|!?\[[^\]]*\]\([^)]+\))/g).map((part,i)=>{
 if(part.startsWith('**'))return <strong key={i}>{part.slice(2,-2)}</strong>;
 if(part.startsWith('`'))return <code key={i}>{part.slice(1,-1)}</code>;
 const link=part.match(/^(!?)\[([^\]]*)\]\(([^)]+)\)$/);if(link){if(link[1])return <a key={i} href={safeLink(link[3],path)} target="_blank" rel="noreferrer">{link[2]} <ExternalLink size={12} className="inline"/></a>;return <a key={i} href={safeLink(link[3],path)} target="_blank" rel="noreferrer">{link[2]}</a>;}return part;
 });}
function Markdown({text,path}:{text:string;path:string}) {const lines=text.split('\n');const blocks:React.ReactNode[]=[];for(let i=0;i<lines.length;i++){const l=lines[i];if(!l.trim()||l.startsWith('<!--')||l.startsWith('<details')||l.startsWith('</details'))continue;
 if(l.startsWith('```')){const code=[];while(++i<lines.length&&!lines[i].startsWith('```'))code.push(lines[i]);blocks.push(<pre key={i}><code>{code.join('\n')}</code></pre>);continue;}
 if(l.startsWith('|')&&lines[i+1]?.match(/^\|[\s:|-]+\|/)){const cells=(x:string)=>x.trim().replace(/^\||\|$/g,'').split('|').map(x=>x.trim());const heads=cells(l);i+=2;const rows=[];while(i<lines.length&&lines[i].startsWith('|'))rows.push(cells(lines[i++]));i--;blocks.push(<Table key={i}><TableHeader><TableRow>{heads.map((h,j)=><TableHead key={j}>{inline(h,path)}</TableHead>)}</TableRow></TableHeader><TableBody>{rows.map((r,k)=><TableRow key={k}>{r.map((c,j)=><TableCell key={j}>{inline(c,path)}</TableCell>)}</TableRow>)}</TableBody></Table>);continue;}
 const heading=l.match(/^(#{1,6}) (.*)/);if(heading){const id=heading[2].toLowerCase().replace(/[^a-z0-9 -]/g,'').replace(/ /g,'-');blocks.push(React.createElement(`h${heading[1].length}`,{key:i,id},inline(heading[2],path)));continue;}
 if(l.startsWith('<summary>')){blocks.push(<h3 key={i}>{l.replace(/<[^>]*>/g,'')}</h3>);continue;}
 if(l.match(/^[-*] /)){blocks.push(<p className="report-bullet" key={i}>{inline(l.slice(2),path)}</p>);continue;}
 blocks.push(<p key={i}>{inline(l,path)}</p>);
 }return <>{blocks}</>;}
