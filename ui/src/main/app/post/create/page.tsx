"use client";

import {useState} from "react";
import {ToastContainer, toast} from 'react-toast';
import {useMsal} from "@azure/msal-react";
import Link from "next/link";
import getAccessToken from "@/app/getAccessToken";
import buildJSONHeaders from "@/app/buildJSONHeaders";

export default function PostCreatePage() {
    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");
    const [success, setSuccess] = useState(false);
    const [postId, setPostId] = useState("");
    const [postType, setPostType] = useState("text");

    async function createPost() {
        if (!title) {
            toast.info("Please provide a title to your post.");
            return;
        }

        const accessToken = await getAccessToken();
        if (accessToken === null) {
            toast.error("Failed to get your access token.");
            return;
        }

        const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post/`, {
            method: 'POST',
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ title, body }),
        });

        if (res.ok) {
            const data = await res.json();
            toast.success("Post created successfully.");
            setSuccess(true);
            setPostId(data.id);
        }
    }

    return (
        <main className="flex w-screen h-screen justify-center items-center">
            <div
                className="flex w-1/2 flex-col p-2 gap-2 shadow-reddit border border-reddit-postline">
                <h1 className="self-center">Create a post</h1>
                <br/>
                <ToastContainer delay={8000}/>
                <input
                    className="border border-reddit-postline rounded-sm p-2"
                    type="text"
                    placeholder="Title"
                    onChange={e => setTitle(e.currentTarget.value)}
                    disabled={success}/>
                <textarea
                    className="border border-reddit-postline rounded-sm p-2"
                    placeholder="Text (optional)"
                    onChange={e => setBody(e.currentTarget.value)}
                    rows={6}
                    disabled={success}/>
                <button className="p-2 rounded-sm bg-reddit-orange text-white w-full"
                        onClick={createPost}
                        disabled={success}
                        hidden={success}>Post
                </button>
                {success && (
                    <Link href={`/post/${postId}`}>
                        <button className="p-2 w-full rounded-sm bg-green-400 text-white">
                            See post
                        </button>
                    </Link>
                )}
            </div>
        </main>
    )
}