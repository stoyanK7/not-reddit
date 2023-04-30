import PostActions from "./PostActions";
import PostBody from "./PostBody";
import PostInfo from "./PostInfo";
import PostTitle from "./PostTitle";

export default function PostItem({ post, mutate }) {
    return (
        <div
            className="grid grid-rows-[auto_auto_1fr_auto] grid-cols-1 gap-2 bg-white
            rounded-sm p-2 shadow-reddit border border-reddit-postline">
            <PostInfo
                username={post.username}
                postedAt={post.posted_at} />
            <PostTitle
                title={post.title} />
            <PostBody
                body={post.body} />
            <PostActions
                id={post.id}
                votes={post.votes}
                username={post.username}
                mutate={mutate} />
        </div>
    );
}
