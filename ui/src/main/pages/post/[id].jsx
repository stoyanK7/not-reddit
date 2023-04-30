import { toast } from "react-toast";

import CommentList from "@/components/CommentList";
import CreateComment from "@/components/CreateComment";
import PostItem from "@/components/PostItem";

async function getPost(id) {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/api/post/${id}`);
    return res.json();
}

async function getComments(postId) {
    // const res: Response = await fetch(`${process.
    // env.NEXT_PUBLIC_API_SERVICE_URL}/comment/${postId}`);
    // return res.json();
}

export default async function PostPage({ params }) {
    const postData = getPost(params.id);
    const commentsData = getComments(params.id);

    const [post, comments] = await Promise.all([postData, commentsData]);

    return (
        <main
            className="flex w-screen h-screen justify-center items-center">
            <div
                className="flex flex-col p-2 gap-2">
                <PostItem
                    post={post} />
                <CreateComment
                    postId={post.id} />
                {/* <CommentList comments={comments} /> */}
            </div>
        </main>
    );
}
