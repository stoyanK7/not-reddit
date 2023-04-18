import CreatePost from "./CreatePost";
import PostList from "@/app/PostList";

export default function Home() {
  return (
    <main className="w-1/2 mx-auto min-w-fit my-2">
      <CreatePost />
      <PostList />
    </main>
  )
}
