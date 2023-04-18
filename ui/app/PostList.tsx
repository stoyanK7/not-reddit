import Post from "@/app/Post";

export default async function PostList() {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post/`);
    const posts = await res.json();

    return (
        <div className="flex flex-col gap-2">
            {posts.map((post: any) => (
                <Post key={post.id} post={post} />
            ))}
        </div>
    )
}
