import { AuthenticatedTemplate } from "@azure/msal-react";
import { useState } from "react";
import { toast } from "react-toast";
import useSWR from "swr";

import CreatePost from "@/components/CreatePost";
import PostList from "@/components/PostList";
import fetcher from "@/utils/fetcher";
import fromApi from "@/utils/fromApi";


export default function Home() {
    const [sortBy, setSortBy] = useState("hot");

    const { data: posts, error, isLoading, mutate } = useSWR(
        [fromApi(`/api/post?sort_by=${sortBy}`), null],
        fetcher);

    if (error) {
        toast.error("Failed to load latest posts");
    }
    if (isLoading) return <div>loading...</div>;

    return (
        <main
            className="w-1/2 mx-auto min-w-fit my-2 mt-24 gap-2">
            <AuthenticatedTemplate>
                <CreatePost />
            </AuthenticatedTemplate>
            <div
                className="flex gap-2 w-full bg-white p-2">
                <div
                    onClick={() => setSortBy("latest")}
                    className={`p-2 text-green-600 rounded-sm hover:bg-green-300
                    hover:cursor-pointer ${sortBy === "latest" ? "bg-green-300" : ""}`}>
                    Latest
                </div>
                <div
                    onClick={() => setSortBy("hot")}
                    className={`p-2 text-orange-600 rounded-sm hover:bg-orange-300
                    hover:cursor-pointer ${sortBy === "hot" ? "bg-orange-300" : ""}`}>
                    Hot
                </div>
            </div>
            {posts &&
                <PostList
                    mutate={mutate}
                    posts={posts} />
            }
        </main>
    );
}
