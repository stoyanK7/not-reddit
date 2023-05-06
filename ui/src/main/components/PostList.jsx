import Link from "next/link";
import { toast } from "react-toast";
import useSWR from "swr";

import PostItem from "@/components/PostItem";
import fetcher from "@/utils/fetcher";
import fromApi from "@/utils/fromApi";

export default function PostList({ page, sortBy, setCanShowMore }) {
    const { data: posts, error, isLoading, mutate } = useSWR(
        [fromApi(`/api/post?sort_by=${sortBy}&page=${page}`), null],
        fetcher);

    if (error) {
        toast.error("Failed to load latest posts");
    }
    if (isLoading) return <div>loading...</div>;

    if (posts.length === 0 || posts.length < 10) {
        setCanShowMore(false);
    }

    return (
        <div
            className="flex flex-col gap-2 my-2">
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
