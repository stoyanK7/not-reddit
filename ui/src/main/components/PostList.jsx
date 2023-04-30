import PostItem from "@/components/PostItem";

export default function PostList({ posts, mutate }) {
    return (
        <div
            className="flex flex-col gap-2">
            {posts.map((post) => (
                <PostItem
                    key={post.id}
                    post={post}
                    mutate={mutate} />
            ))}
        </div>
    );
}
