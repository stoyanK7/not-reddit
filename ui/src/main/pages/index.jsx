import { AuthenticatedTemplate } from "@azure/msal-react";
import { toast } from "react-toast";
import useSWR from "swr";

import CreatePost from "@/components/CreatePost";
import PostList from "@/components/PostList";
import fetcher from "@/utils/fetcher";
import fromApi from "@/utils/fromApi";


export default function Home() {
    const { data: posts, error, isLoading, mutate } = useSWR([fromApi("/api/post"), null],
        fetcher);

    if (error) {
        toast.error("Failed to load latest posts");
    }
    if (isLoading) return <div>loading...</div>;

    return (
        <main
            className="w-1/2 mx-auto min-w-fit my-2 mt-24">
            <AuthenticatedTemplate>
                <CreatePost />
            </AuthenticatedTemplate>
            {posts &&
                <PostList
                    mutate={mutate}
                    posts={posts} />
            }
        </main>
    );
}
