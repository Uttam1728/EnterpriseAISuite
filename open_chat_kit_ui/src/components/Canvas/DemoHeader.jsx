import { Flex } from "@mantine/core";
import { IconArrowsDiagonalMinimize2 } from "@tabler/icons-react";
import React from "react";

function DemoHeader() {
  return (
    <>
      <Flex direction="row" justify="start">
        Manu's Computer
      </Flex>
      <Flex direction="row" justify="end">
        <IconArrowsDiagonalMinimize2 stroke={2} />
      </Flex>
    </>
  );
}

export default DemoHeader;
