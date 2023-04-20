"use client";

import { useState } from "react";
import { ToastContainer, toast } from 'react-toast';


export default function CreateComment({ postId }: { postId: string }) {
    const [commentBody, setCommentBody] = useState("");

    async function publishComment() {
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/comment`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ commentBody, "post_id": postId, "user_id": 1 }),
        });
        if (res.ok) {
            const data = await res.json();
            toast.success("Post created successfully.");
        }
    }

    return (
        <div className="flex flex-col gap-2">
            <ToastContainer delay={8000}/>
            <span>Comment on the post</span>
            <textarea rows={10}
                onChange={e => setCommentBody(e.currentTarget.value)}
                placeholder="What are your thoughts?"
                className="bg-white px-4 py-2 rounded-sm border border-reddit-postline" />
            <button className="bg-reddit-orange p-2 rounded-sm text-white"
                onClick={publishComment}>Comment</button>
        </div>
    )
}