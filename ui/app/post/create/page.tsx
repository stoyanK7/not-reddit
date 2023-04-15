"use client";

import { useState } from "react";
import { ToastContainer, toast } from 'react-toast'

export default function CreatePost() {

    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");
    const [status, setStatus] = useState(false);

    async function createPost() {
        if (!title) {
            alert("Please enter a title");
            return;
        }


        const response: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, body }),
        });

        if (response.ok) {
            toast.success("Post created successfully.");
        }
    }

    return (
        <div className="flex flex-col">
            <h1>Create a post</h1>
            <br />
            <ToastContainer />
            <input
                type="text"
                placeholder="Title"
                onChange={e => setTitle(e.currentTarget.value)} />
            <input
                type="text"
                placeholder="Text (optional)"
                onChange={e => setBody(e.currentTarget.value)} />
            <button onClick={createPost}>Post</button>
        </div>
    )
}