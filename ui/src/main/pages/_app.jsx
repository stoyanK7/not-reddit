import "@/styles/globals.css";

import { MsalProvider } from "@azure/msal-react";
import Head from "next/head";

import Layout from "@/components/Layout";
import { msalInstance } from "@/utils/authConfig";

export default function App({ Component, pageProps }) {
    return (
        <>
            <Head>
                <title>not-reddit</title>
            </Head>
            <MsalProvider
                instance={msalInstance}>
                <Layout>
                    <Component
                        {...pageProps} />
                </Layout>
            </MsalProvider>
        </>
    );
}
