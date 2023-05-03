import { useRouter } from "next/router";
import { toast } from "react-toast";
import useSWR from "swr";

import CommentList from "@/components/CommentList";
import CreateComment from "@/components/CreateComment";
import PostItem from "@/components/PostItem";
import fetcher from "@/utils/fetcher";
import fromApi from "@/utils/fromApi";

export default function PostPage() {
    const router = useRouter();
    const { id } = router.query;

    const { data: post, error: postError, isLoading: postIsLoading, mutate: postMutate } = useSWR(
        [fromApi(`/api/post/${id}`), null], fetcher
    );

    const { data: comments, error: commentsError, isLoading: commentsIsLoading, mutate } = useSWR(
        // TODO: Implement pagination
        [fromApi(`/api/comment?post_id=${id}&page=0`), null], fetcher
    );

    if (postError) {
        toast.error("Failed to load post");
    }

    if (commentsError) {
        toast.error("Failed to load comments");
    }

    return (
        <main
            className="flex w-screen min-h-screen justify-center items-center mt-24">
            <div
                className="flex flex-col p-2 gap-2 w-1/2">
                {postIsLoading && <p>Loading post...</p>}
                {post &&
                    <>
                        <PostItem
                            post={post}
                            mutate={postMutate} />
                        <CreateComment
                            postId={post.id}
                            mutate={mutate} />
                    </>
                }
                {commentsIsLoading && <p>Loading comments...</p>}
                {comments &&
                     <CommentList
                         comments={comments} />
                }
            </div>
        </main>
    );
}
