import React from "react";
import Canvas from "./Canvas";
import DemoHeader from "./DemoHeader";

export default function CanvasContainer() {
  return (
    <div className="h-full !max-w-[-webkit-fill-available]">
      <Canvas headerContent={<DemoHeader />} />
    </div>
  );
}
