"use client";

import { ToastContainer, toast } from "react-toast";
import PostItem from "@/app/post/PostItem";
import CommentList from "@/app/CommentList";
import CreateComment from "@/app/CreateComment";

async function getPost(id: string) {
    const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/post/${id}`);
    return res.json();
}

async function getComments(postId: string) {
    // const res: Response = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/comment/${postId}`);
    // return res.json();
}

export default async function PostPage({ params }: { params: { id: string } }) {
    const postData = getPost(params.id);
    const commentsData = getComments(params.id);

    const [post, comments] = await Promise.all([postData, commentsData]);

    return (
        <main className="flex w-screen h-screen justify-center items-center">
            <div className="flex flex-col p-2 gap-2">
                <ToastContainer delay={8000}/>
                <PostItem post={post} />
                <CreateComment postId={post.id} />
                {/* <CommentList comments={comments} /> */}
            </div>
        </main>
    )
}