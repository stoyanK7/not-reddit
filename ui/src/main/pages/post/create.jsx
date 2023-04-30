import Link from "next/link";
import { useRouter } from "next/router";
import { useState } from "react";
import { Tab, TabList, TabPanel, Tabs } from "react-tabs";
import { toast, ToastContainer } from "react-toast";

import ImageTab from "@/components/ImageTab";
import TextTab from "@/components/TextTab";
import buildAuthorizationHeader from "@/utils/buildAuthorizationHeader";
import buildJSONHeaders from "@/utils/buildJSONHeaders";
import fromApi from "@/utils/fromApi";
import getAccessToken from "@/utils/getAccessToken";

export default function PostCreatePage() {
    const router = useRouter();
    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");
    const [id, setId] = useState("");
    const [type, setType] = useState(router.query.type || "text");
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

        if (type === "image") {
            await createImagePost(accessToken);
        }

        if (type === "text") {
            await createTextPost(accessToken);
        }
    }

    async function createTextPost(accessToken) {
        const res = await fetch(fromApi("/api/post/text"), {
            method: "POST",
            headers: buildJSONHeaders(accessToken),
            body: JSON.stringify({ title, body }),
        });
        await handleResponse(res);
    }

    async function createImagePost(accessToken) {
        const formData = new FormData();
        formData.append("title", title);
        formData.append("file", body);
        const res = await fetch(fromApi("/api/post/image"), {
            method: "POST",
            // Image requests should't have content type explicitly set.
            headers: buildAuthorizationHeader(accessToken),
            body: formData,
        });
        await handleResponse(res);
    }

    async function handleResponse(res) {
        if (res.ok) {
            const data = await res.json();
            toast.success("Post created successfully.");
            setSuccess(true);
            setId(data.id);
        } else {
            toast.error("Something went wrong");
        }
    }

    return (
        <main
            className="flex w-screen h-screen justify-center items-center">
            <ToastContainer
                delay={8000} />
            <Tabs
                className="flex w-1/2 flex-col p-2 gap-2 shadow-reddit border bg-white
                border-reddit-postline"
                selectedIndex={type === "text" ? 0 : 1}>
                <TabList
                    className="flex justify-around">
                    <Tab
                        className="py-2 px-4 rounded-sm text-2xl hover:bg-reddit-gray-hover
                            grow-0"
                        onClick={() => setType("text")}>
                        Text
                    </Tab>
                    <Tab
                        className="py-2 px-4 rounded-sm text-2xl hover:bg-reddit-gray-hover
                            grow-0"
                        onClick={() => setType("image")}>
                        Image
                    </Tab>
                </TabList>
                <h1
                    className="self-center text-4xl">Create a post</h1>
                <br />
                <input
                    className="border border-reddit-postline rounded-sm p-2"
                    type="text"
                    placeholder="Title"
                    onChange={e => setTitle(e.currentTarget.value)}
                    disabled={success} />
                <TabPanel
                    className="flex-grow">
                    <TextTab
                        setBody={setBody} success={success} />
                </TabPanel>
                <TabPanel
                    className="flex-grow">
                    <ImageTab
                        setBody={setBody} success={success} />
                </TabPanel>
                <button
                    className="p-2 rounded-sm bg-reddit-orange text-white w-full"
                    onClick={createPost}
                    disabled={success}
                    hidden={success}>
                    Post
                </button>
                {success && (
                    <Link
                        href={`/post/${id}`}>
                        <button
                            className="p-2 w-full rounded-sm bg-green-400 text-white">
                            See post
                        </button>
                    </Link>
                )}
            </Tabs>
        </main>
    );
}
