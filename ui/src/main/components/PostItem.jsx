import PostActions from "@/components/PostActions";
import PostBody from "@/components/PostBody";
import PostInfo from "@/components/PostInfo";
import PostTitle from "@/components/PostTitle";

export default function PostItem({ post, mutate }) {
    return (
        <div
            className="grid grid-rows-[auto_auto_1fr_auto] grid-cols-1 gap-2 bg-white
            rounded-sm p-2 shadow-reddit border border-reddit-postline w-full">
            <PostInfo
                username={post.username}
                silverAwards={post.silver_awards}
                goldAwards={post.gold_awards}
                platinumAwards={post.platinum_awards}
                postedAt={post.posted_at} />
            <PostTitle
                title={post.title} />
            <PostBody
                body={post.body}
                type={post.post_type} />
            <PostActions
                id={post.id}
                votes={post.votes}
                username={post.username}
                mutate={mutate} />
        </div>
    );
}
