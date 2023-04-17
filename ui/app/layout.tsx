"use client";

import './globals.css'
import React from "react";
import { Configuration, PublicClientApplication } from "@azure/msal-browser";
import { MsalProvider } from "@azure/msal-react";


const msalConfig: Configuration = {
  auth: {
    clientId: "d448d19c-b7c3-4c1f-8c1b-e726b3a3ba88",
    redirectUri: "http://localhost:3000",
  },

};

const msalClient = new PublicClientApplication(msalConfig);

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <MsalProvider instance={msalClient}>
        <body>{children}</body>
      </MsalProvider>
    </html>
  )
}
