import { useRouter } from "next/router";
import { toast } from "react-toast";
import useSWR from "swr";

import PostItem from "@/components/PostItem";
import fetcher from "@/utils/fetcher";
import fromApi from "@/utils/fromApi";

export default function PostPage() {
    const router = useRouter();
    const { id } = router.query;

    const { data: post, error: postError, isLoading: postIsLoading, mutate: postMutate } = useSWR(
        [fromApi(`/api/post/${id}`), null], fetcher
    );

    if (postError) {
        toast.error("Failed to load post");
    }

    return (
        <main
            className="flex w-screen h-screen justify-center items-center">
            <div
                className="flex flex-col p-2 gap-2 w-1/2">
                {postIsLoading && <p>Loading post...</p>}
                {post &&
                    <PostItem
                        post={post}
                        mutate={postMutate} />
                }
                {/*<CreateComment*/}
                {/*    postId={post.id} />*/}
                {/* <CommentList comments={comments} /> */}
            </div>
        </main>
    );
}
