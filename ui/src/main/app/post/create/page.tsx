"use client";

import {useState} from "react";
import {ToastContainer, toast} from 'react-toast';
import Link from "next/link";
import getAccessToken from "@/app/getAccessToken";
import buildJSONHeaders from "@/app/buildJSONHeaders";
import {Tab, Tabs, TabList, TabPanel} from 'react-tabs';
import TextTab from "@/app/post/create/TextTab";
import ImageTab from "@/app/post/create/ImageTab";
import buildAuthorizationHeader from "@/app/buildAuthorizationHeader";

export default function PostCreatePage({searchParams}: { searchParams: { type: string } }) {
    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");
    const [id, setId] = useState("");
    const [type, setType] = useState(searchParams?.type || "text");
    const [success, setSuccess] = useState(false);

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

        let headers = buildJSONHeaders(accessToken);

        // Image should not have content-type header.
        if (type === "image") {
            headers = buildAuthorizationHeader(accessToken);
        }

        const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/api/post`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({title, body}),
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
            <ToastContainer delay={8000}/>
            <Tabs className="flex w-1/2 flex-col p-2 gap-2 shadow-reddit border
                border-reddit-postline">
                <TabList className="flex justify-around">
                    <Tab className="py-2 px-4 rounded-sm text-2xl hover:bg-reddit-gray-hover
                            grow-0"
                         onClick={() => setType("text")}>
                        Text
                    </Tab>
                    <Tab className="py-2 px-4 rounded-sm text-2xl hover:bg-reddit-gray-hover
                            grow-0"
                         onClick={() => setType("image")}>
                        Image
                    </Tab>
                </TabList>
                <h1 className="self-center text-4xl">Create a post</h1>
                <br/>
                <input
                    className="border border-reddit-postline rounded-sm p-2"
                    type="text"
                    placeholder="Title"
                    onChange={e => setTitle(e.currentTarget.value)}
                    disabled={success}/>
                <TabPanel className="flex-grow">
                    <TextTab setBody={setBody} success={success}/>
                </TabPanel>
                <TabPanel className="flex-grow">
                    <ImageTab setBody={setBody} success={success}/>
                </TabPanel>
                <button className="p-2 rounded-sm bg-reddit-orange text-white w-full"
                        onClick={createPost}
                        disabled={success}
                        hidden={success}>
                    Post
                </button>
                {success && (
                    <Link href={`/post/${id}`}>
                        <button className="p-2 w-full rounded-sm bg-green-400 text-white">
                            See post
                        </button>
                    </Link>
                )}
            </Tabs>
        </main>
    )
}