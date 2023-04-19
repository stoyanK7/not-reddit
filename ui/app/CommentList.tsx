import CommentItem from "@/app/CommentItem"

export default function CommentList({ comments }: { comments: object[] }) {
    return (
        <div className="flex flex-col gap-2">
            {comments.map(comment => (
                <CommentItem key={comment.id} comment={comment} />
            ))}
        </div>
    )
}
