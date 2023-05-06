import { AuthenticatedTemplate } from "@azure/msal-react";
import { useState } from "react";

import CreatePost from "@/components/CreatePost";
import PostList from "@/components/PostList";


export default function Home() {
    const [page, setPage] = useState(0);
    const [sortBy, setSortBy] = useState("hot");
    const [canShowMore, setCanShowMore] = useState(true);

    const postsPages = [];
    for (let i = 0; i <= page; i++) {
        postsPages.push(
            <PostList
                setCanShowMore={setCanShowMore}
                canShowMore={canShowMore}
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
            <div
                className="flex gap-2 w-full bg-white p-2">
                <div
                    onClick={() => setSortBy("latest")}
                    className={`p-2 text-green-600 rounded-sm hover:bg-green-300
                    hover:cursor-pointer ${sortBy === "latest" ? "bg-green-300" : ""}`}>
                    Latest
                </div>
                <div
                    onClick={() => setSortBy("hot")}
                    className={`p-2 text-orange-600 rounded-sm hover:bg-orange-300
                    hover:cursor-pointer ${sortBy === "hot" ? "bg-orange-300" : ""}`}>
                    Hot
                </div>
            </div>
            {postsPages}
            {canShowMore &&
                <button
                    className="w-full p-2 rounded-sm bg-reddit-orange text-white"
                    onClick={() => setPage(page + 1)}>
                    Load more
                </button>
            }
            {!canShowMore &&
                <span>There are no more posts.</span>
            }
        </main>
    );
}
