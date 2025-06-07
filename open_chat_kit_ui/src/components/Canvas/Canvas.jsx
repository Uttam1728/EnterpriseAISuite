import React from "react";
import DemoHeader from "./DemoHeader";

function Canvas({ headerClass, headerContent }) {
  // const currentBlock = blocks.find((b) => b.id === activeTabId);
  return (
    <div className="flex flex-col h-full overflow-hidden px-4 pt-3 pb-4">
      <div
        className={`flex justify-between px-1 bg-codeHeader items-center rounded-t-lg border border-borderDefault border-b-0 max-w-3/4 ${headerClass}`}
      >
        {headerContent}
      </div>
    </div>
  );
}

export default Canvas;
