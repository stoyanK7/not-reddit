import Link from "next/link";

import PostItem from "@/components/PostItem";

export default function PostList({ posts, mutate }) {
    return (
        <div
            className="flex flex-col gap-2">
            {posts.map((post) => (
                <Link
                    key={post.id}
                    href={`/post/${post.id}`}>
                    <PostItem
                        post={post}
                        mutate={mutate} />
                </Link>
            ))}
        </div>
    );
}
