import CommentItem from "@/components/CommentItem";

export default function CommentList({ comments }) {
    return (
        <div
            className="flex flex-col gap-2">
            {comments.map(comment => (
                <CommentItem
                    key={comment.id}
                    comment={comment} />
            ))}
        </div>
    );
}
