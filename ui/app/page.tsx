import CreatePost from "./CreatePost";
import Post from "./Post";

export default async function Home() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post/`);
  const posts = await res.json();

  return (
    <main className="">
      <CreatePost />
      <div className="flex flex-col gap-2">
        {posts.map((post: any) => (
          <Post key={post.id} post={post} />
        ))}
      </div>
    </main>
  )
}
