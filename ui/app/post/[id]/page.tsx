"use client";

import { ToastContainer, toast } from "react-toast";
import { useSearchParams } from 'next/navigation';
import Post from "@/app/Post";

async function getPost(id: string) {
    const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post/${id}`);
    return res.json();
}

async function getComments(postId: string) {
    // const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/comment/${postId}`);
    // return res.json();
}

export default async function PostPage({ params }: { params: { id: string } }) {
    const searchParams = useSearchParams();
    const postData = getPost(params.id);
    const commentsData = getComments(params.id);

    const [post, comments] = await Promise.all([postData, commentsData]);

    // useEffect(() => {
    //     console.log("here")
    //     console.log(searchParams.toString());
    if (searchParams.toString().includes("created=true")) {
        toast.success("Post created successfully.");
    }
    // }, [searchParams])

    return (
        <main className="flex w-screen h-screen justify-center items-center">
            <div className="flex flex-col p-2 gap-2">
                <ToastContainer />
                <Post post={post} />
                <CommentList comments={comments} />
            </div>
        </main>
    )
}