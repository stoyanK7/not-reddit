"use client"

import CreatePost from "./CreatePost";
import PostList from "@/app/post/PostList";
import {AuthenticatedTemplate} from "@azure/msal-react";

export default function Home() {
    return (
        <main className="w-1/2 mx-auto min-w-fit my-2">
            <AuthenticatedTemplate>
                <CreatePost/>
            </AuthenticatedTemplate>
            {/* @ts-ignore */}
            <PostList/>
        </main>
    )
}
