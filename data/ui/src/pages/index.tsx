import Head from "next/head";
import Image from "next/image";
import localFont from "next/font/local";
import styles from "@/styles/Home.module.css";
import WorldMap from "@/components/WorldMap";

export default function Home() {
  return (
    <>
      <div style={{height: '100vh', overflow: 'hidden', width: '100%', background: 'white', padding: '50px', display: 'flex', flexDirection: 'column', gap: '20px'}}>
        <h1 style={{color: 'black'}}>
          Dataset Creator Tool
        </h1>
        <div style={{width: '100%', display: 'flex', justifyContent: 'center'}}>
        <WorldMap/>
        </div>
        
      </div>
    </>
  );
}
