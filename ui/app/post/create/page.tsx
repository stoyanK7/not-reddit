"use client";

import { useState } from "react";
import { ToastContainer, toast } from 'react-toast';
import { useMsal } from "@azure/msal-react";
import { InteractionRequiredAuthError } from "@azure/msal-browser";
import { loginRequest } from "@/app/loginRequest";


export default function CreatePost() {
    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");
    const [status, setStatus] = useState(false);
    const { instance, accounts } = useMsal();

    async function createPost() {
        if (!title) {
            alert("Please enter a title");
            return;
        }

        console.log(instance.getActiveAccount());
        instance.setActiveAccount(accounts[0]);

        instance.acquireTokenSilent(loginRequest)
            .then(async tokenResponse => {
                console.log("here");
                const headers = new Headers();
                const bearer = "Bearer " + tokenResponse.accessToken;
                headers.append("Authorization", bearer);
                const options = {
                    method: "POST",
                    headers: headers,
                    body: JSON.stringify({ title, body })
                };

                const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post`, options);
                const data = await res.json();
                console.log(data);

                if (res.ok) {
                    toast.success("Post created successfully.");
                }
            }).catch(async (error) => {
                console.log(error);
                if (error instanceof InteractionRequiredAuthError) {
                    return instance.acquireTokenPopup(loginRequest);
                }
            })

        // const response: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post`, {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify({ title, body }),
        // });


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