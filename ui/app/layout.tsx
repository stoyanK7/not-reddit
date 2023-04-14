import './globals.css'
import React from "react";

export const metadata = {
    title: 'not-reddit',
    description: 'not-reddit is a social news aggregation platform with sub-communities, ' +
        'messaging, and awards that allows users to post and share content, vote on submissions, ' +
        'and comment on posts.',
}

export default function RootLayout({
                                       children,
                                   }: {
    children: React.ReactNode
}) {
    return (
        <html lang="en">
        <body>{children}</body>
        </html>
    )
}
