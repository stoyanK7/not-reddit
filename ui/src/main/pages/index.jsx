import { AuthenticatedTemplate } from "@azure/msal-react";
import { useState } from "react";

import CreatePost from "@/components/CreatePost";
import LoadMore from "@/components/LoadMore";
import PostList from "@/components/PostList";
import SortBy from "@/components/SortBy";


export default function Home() {
    const [page, setPage] = useState(0);
    const [sortBy, setSortBy] = useState("hot");
    const [canLoadMore, setCanLoadMore] = useState(true);

    const postsPages = [];
    for (let i = 0; i <= page; i++) {
        postsPages.push(
            <PostList
                setCanLoadMore={setCanLoadMore}
                page={i}
                sortBy={sortBy}
                key={i} />
        );
    }

    return (
        <main
            className="w-1/2 mx-auto min-w-fit my-2 mt-24 gap-2">
            <AuthenticatedTemplate>
                <CreatePost />
            </AuthenticatedTemplate>
            <SortBy
                sortBy={sortBy}
                setSortBy={setSortBy} />
            {postsPages}
            <LoadMore
                canLoadMore={canLoadMore}
                page={page}
                setPage={setPage} />
        </main>
    );
}
