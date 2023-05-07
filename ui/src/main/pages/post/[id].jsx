import { useRouter } from "next/router";
import { useState } from "react";
import { toast } from "react-toast";
import useSWR from "swr";

import CommentList from "@/components/CommentList";
import CreateComment from "@/components/CreateComment";
import LoadMore from "@/components/LoadMore";
import PostItem from "@/components/PostItem";
import fetcher from "@/utils/fetcher";
import fromApi from "@/utils/fromApi";
import SortBy from "@/components/SortBy";
import { AuthenticatedTemplate } from "@azure/msal-react";

export default function PostPage() {
    const router = useRouter();
    const { id } = router.query;
    const [page, setPage] = useState(0);
    const [sortBy, setSortBy] = useState("hot");
    const [canLoadMore, setCanLoadMore] = useState(true);

    const { data: post, error: postError, isLoading: postIsLoading, mutate: postMutate } = useSWR(
        [fromApi(`/api/post/${id}`), null], fetcher
    );

    const commentsPages = [];
    for (let i = 0; i <= page; i++) {
        commentsPages.push(
            <CommentList
                setCanLoadMore={setCanLoadMore}
                canLoadMore={canLoadMore}
                page={i}
                postId={id}
                sortBy={sortBy}
                key={i} />
        );
    }

    if (postError) {
        toast.error("Failed to load post");
    }

    return (
        <main
            className="flex w-screen min-h-screen justify-center items-center mt-24">
            <div
                className="flex flex-col p-2 gap-2 w-1/2">
                {postIsLoading && <p>Loading post...</p>}
                {post &&
                    <PostItem
                        post={post}
                        mutate={postMutate} />
                }
                <AuthenticatedTemplate>
                    <CreateComment
                        postId={id} />
                </AuthenticatedTemplate>

                <SortBy
                    sortBy={sortBy}
                    setSortBy={setSortBy} />
                {commentsPages}
                <LoadMore
                    canLoadMore={canLoadMore}
                    page={page}
                    setPage={setPage} />
            </div>
        </main>
    );
}
