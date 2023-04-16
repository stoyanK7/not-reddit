"use client";

import Link from "next/link";

export default function PostActions({ id }: { id: number }) {
    function upvote() {
        // TODO: implement call
        // TODO: give visual feedback
    }

    function downvote() {
        // TODO: implement call
        // TODO: give visual feedback
    }
    return (
        <div className="flex gap-2 text-reddit-gray hover:cursor-pointer">
            <div className="flex items-center">
                <span className="p-2 mr-1 rounded-sm hover:bg-reddit-gray-hover
                    hover:text-reddit-orange"
                    onClick={upvote}>
                    Up
                </span>
                <span className="font-bold text-reddit-black">134</span>
                <span className="p-2 ml-1 rounded-sm hover:bg-reddit-gray-hover
                    hover:text-reddit-blue"
                    onClick={downvote}>
                    Down
                </span>
            </div>
            <Link href={`/post/${id}`}>
                <div className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                    Comments
                </div>
            </Link>
            <div className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Award
            </div>
            <div className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Share
            </div>
            <div className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Save
            </div>
        </div>
    )
}