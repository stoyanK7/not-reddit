"use client";

import React from "react";
import { MsalProvider } from "@azure/msal-react";
import '@/app/globals.css'
import { msalInstance } from '@/app/authConfig';


export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <MsalProvider instance={msalInstance}>
      <html lang="en">
        <body>{children}</body>
      </html>
    </MsalProvider>
  )
}
