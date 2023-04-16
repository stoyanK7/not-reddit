import PostInfo from "./PostInfo";
import PostTitle from "./PostTitle";
import PostBody from "./PostBody";
import PostActions from "./PostActions";

export default function Post({ post }: { post: any }) {
    return (
        <div className="grid grid-rows-[auto_auto_1fr_auto] grid-cols-1 gap-2 bg-white
            rounded-sm p-2 border border-not-reddit-postline">
            <PostInfo subreddit={post.subreddit} username={post.username} postedAt={post.posted_at} />
            <PostTitle title={post.title} />
            <PostBody body={post.body} />
            <PostActions id={post.id}  />
        </div>
    )
}
