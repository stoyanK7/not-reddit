import PostItem from "@/components/PostItem";

export default function PostList({ posts }) {
    return (
        <div
            className="flex flex-col gap-2">
            {posts.map((post) => (
                <PostItem
                    key={post.id}
                    post={post} />
            ))}
        </div>
    );
}
