import CommentActions from "@/components/CommentActions";
import CommentBody from "@/components/CommentBody";
import CommentInfo from "@/components/CommentInfo";

export default function CommentItem({ comment, mutate }) {
    // TODO: add votes field in comment model
    comment.votes = 0;
    return (
        <div
            className="grid grid-rows-[auto_1fr_auto] grid-cols-1 gap-2 bg-white
            rounded-sm p-2 shadow-reddit border border-reddit-postline w-full">
            <CommentInfo
                username={comment.username}
                commentedAt={comment.commented_at} />
            <CommentBody
                body={comment.body} />
            <CommentActions
                mutate={mutate}
                comment_id={comment.id}
                username={comment.username}
                votes={comment.votes} />
        </div>
    );
}
