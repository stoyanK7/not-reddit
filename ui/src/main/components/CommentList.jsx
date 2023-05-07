import { toast } from "react-toast";
import useSWR from "swr";

import CommentItem from "@/components/CommentItem";
import fetcher from "@/utils/fetcher";
import fromApi from "@/utils/fromApi";

export default function CommentList({ postId, page, sortBy, setCanLoadMore }) {
    const { data: comments, error, isLoading, mutate } = useSWR(
        [fromApi(`/api/comment?post_id=${postId}&page=${page}&sort_by=${sortBy}`), null],
        fetcher
    );

    if (error) {
        toast.error("Failed to load comments");
    }
    if (isLoading) return <div>loading...</div>;

    if (comments.length === 0 || comments.length < 10) {
        setCanLoadMore(false);
    }

    return (
        <div
            className="flex flex-col gap-2 my-2">
            {comments.map(comment => (
                <CommentItem
                    key={comment.id}
                    comment={comment}
                    mutate={mutate} />
            ))}
        </div>
    );
}
