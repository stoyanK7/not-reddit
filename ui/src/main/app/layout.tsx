"use client";

import './globals.css'
import React from "react";
import { PublicClientApplication } from "@azure/msal-browser";
import { MsalProvider } from "@azure/msal-react";
import { msalConfig } from '@/app/authConfig';

const msalClient = new PublicClientApplication(msalConfig);

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <MsalProvider instance={msalClient}>
      <html lang="en">
        <body>{children}</body>
      </html>
    </MsalProvider>
  )
}
