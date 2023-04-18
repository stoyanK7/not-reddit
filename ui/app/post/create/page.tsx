"use client";

import { useState } from "react";
import { ToastContainer, toast } from 'react-toast';
import { useMsal } from "@azure/msal-react";
import { InteractionRequiredAuthError } from "@azure/msal-browser";
import { loginRequest } from "@/app/loginRequest";
import { redirect } from 'next/navigation';
import { useRouter } from 'next/navigation';
import Link from "next/link";


export default function PostCreatePage() {
    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");
    const [success, setSuccess] = useState(false);
    const [status, setStatus] = useState(false);
    const { instance, accounts } = useMsal();
    const [id, setId] = useState("");
    const router = useRouter()

    async function createPost() {
        if (!title) {
            toast.info("Title is required.");
            return;
        }

        // console.log(instance.getActiveAccount());
        // instance.setActiveAccount(accounts[0]);

        // instance.acquireTokenSilent(loginRequest)
        //     .then(async tokenResponse => {
        //         console.log("here");
        //         const headers = new Headers();
        //         const bearer = "Bearer " + tokenResponse.accessToken;
        //         headers.append("Authorization", bearer);
        //         const options = {
        //             method: "POST",
        //             headers: headers,
        //             body: JSON.stringify({ title, body })
        //         };

        //         const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post`, options);
        //         const data = await res.json();
        //         console.log(data);

        //         if (res.ok) {
        //             toast.success("Post created successfully.");
        //         }
        //     }).catch(async (error) => {
        //         console.log(error);
        //         if (error instanceof InteractionRequiredAuthError) {
        //             return instance.acquireTokenPopup(loginRequest);
        //         }
        //     })

        const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, body }),
        });

        if (res.ok) {
            const data = await res.json();
            toast.success("Post created successfully.");
            setSuccess(true);
            setId(data.id);
        }
    }

    return (
        <main className="flex w-screen h-screen justify-center items-center">
            <div className="flex w-1/2 flex-col p-2 gap-2 shadow-reddit border border-reddit-postline">
                <h1 className="self-center">Create a post</h1>
                <br />
                <ToastContainer />
                <input
                    className="border border-reddit-postline rounded-sm p-2"
                    type="text"
                    placeholder="Title"
                    onChange={e => setTitle(e.currentTarget.value)}
                    disabled={success} />
                <textarea
                    className="border border-reddit-postline rounded-sm p-2"
                    placeholder="Text (optional)"
                    onChange={e => setBody(e.currentTarget.value)}
                    rows={6}
                    disabled={success} />
                <button className="p-2 rounded-sm bg-reddit-orange text-white w-full"
                    onClick={createPost}
                    disabled={success}
                    hidden={success}>Post</button>
                {success && (
                    <Link href={`/post/${id}`}>
                        <button className="p-2 w-full rounded-sm bg-green-400 text-white">
                            See post
                        </button>
                    </Link>
                )}
            </div>
        </main>
    )
}