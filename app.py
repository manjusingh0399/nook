import React, { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Users, Calendar, Shield, Sparkles } from 'lucide-react';

export default function NookV3(){
 const [page,setPage]=useState('home');
 const nav=['home','member','control'];
 return <div className='min-h-screen bg-black text-white'>
  <header className='border-b border-zinc-800 p-4 flex justify-between items-center'>
   <div className='text-3xl font-black tracking-tight'><span className='text-white'>N</span><span className='text-orange-500'>**</span><span>K</span></div>
   <div className='flex gap-2'>{nav.map(n=><Button key={n} variant='outline' className='border-zinc-700' onClick={()=>setPage(n)}>{n}</Button>)}</div>
  </header>
  {page==='home' && <Home setPage={setPage}/>} 
  {page==='member' && <Member/>}
  {page==='control' && <Control/>}
 </div>
}

function Home({setPage}:{setPage:any}){
 return <main className='p-8 grid md:grid-cols-2 gap-6 items-center'>
  <div>
   <div className='text-orange-500 mb-2'>Your Third Place</div>
   <h1 className='text-6xl font-black leading-tight'>More than plans.<br/>Better than staying in.</h1>
   <p className='text-zinc-400 mt-4 max-w-xl'>Curated social experiences, meaningful rooms, and a premium members ecosystem.</p>
   <div className='mt-6 flex gap-3'>
    <Button className='bg-orange-500 hover:bg-orange-600' onClick={()=>setPage('member')}>Join Nook</Button>
    <Button variant='outline' className='border-zinc-700' onClick={()=>setPage('control')}>Founder OS</Button>
   </div>
  </div>
  <Card className='bg-zinc-950 border-zinc-800 rounded-3xl'><CardContent className='p-8 space-y-4'>
   {['First Out','In Between Plans','Worth It','YHTBT'].map(t=><div key={t} className='p-4 rounded-2xl bg-zinc-900 border border-zinc-800'>{t}</div>)}
  </CardContent></Card>
 </main>
}

function Member(){
 return <div className='p-8 grid md:grid-cols-3 gap-4'>
  {[['Upcoming Events',Calendar],['Community',Users],['Referrals',Sparkles]].map(([t,Icon]:any)=><Card key={t} className='bg-zinc-950 border-zinc-800 rounded-3xl'><CardContent className='p-6'><Icon className='text-orange-500 mb-3'/><div className='text-xl font-bold'>{t}</div><p className='text-zinc-400 mt-2'>Premium member tools and bookings.</p></CardContent></Card>)}
 </div>
}

function Control(){
 return <div className='p-8 space-y-4'>
  <div className='grid md:grid-cols-4 gap-4'>
   {['Applicants','Members','Experiences','Revenue'].map((m,i)=><Card key={m} className='bg-zinc-950 border-zinc-800 rounded-3xl'><CardContent className='p-6'><div className='text-orange-500 text-4xl font-black'>{[12,84,9,'₹42K'][i]}</div><div className='text-zinc-400'>{m}</div></CardContent></Card>)}
  </div>
  <Card className='bg-zinc-950 border-zinc-800 rounded-3xl'><CardContent className='p-6'>
   <div className='flex items-center gap-2 mb-4'><Shield className='text-orange-500'/><span className='font-bold text-xl'>Waitlist Review</span></div>
   <div className='grid md:grid-cols-5 gap-3 text-sm text-zinc-400 mb-2'><div>Name</div><div>Budget</div><div>Availability</div><div>Status</div><div>Action</div></div>
   {['Kabir Anand','Ishita Rao','Dev Sharma'].map(n=><div key={n} className='grid md:grid-cols-5 gap-3 py-3 border-t border-zinc-800 items-center'><div className='text-white'>{n}</div><div>₹400-₹1000</div><div>Weekends</div><div><span className='text-orange-500'>Pending</span></div><div><Button size='sm' className='bg-orange-500'>Approve</Button></div></div>)}
  </CardContent></Card>
 </div>
}
