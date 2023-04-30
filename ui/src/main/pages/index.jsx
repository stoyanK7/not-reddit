import { AuthenticatedTemplate } from "@azure/msal-react";
import { toast, ToastContainer } from "react-toast";
import useSWR from "swr";

import CreatePost from "@/components/CreatePost";
import PostList from "@/components/PostList";
import fetcher from "@/utils/fetcher";
import fromApi from "@/utils/fromApi";


export default function Home() {
    const { data: posts, error, isLoading } = useSWR([fromApi("/api/post"), null], fetcher);

    if (error) {
        toast.error("Failed to load latest posts");
    }
    if (isLoading) return <div>loading...</div>;

    return (
        <main
            className="w-1/2 mx-auto min-w-fit my-2 mt-24">
            <ToastContainer
                delay={8000} />
            <AuthenticatedTemplate>
                <CreatePost />
            </AuthenticatedTemplate>
            {posts &&
                <PostList
                    posts={posts} />
            }
        </main>
    );
}
