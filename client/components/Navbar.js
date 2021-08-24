import {
  Box,
  Text,
  Flex,
  Stack,
  ScaleFade,
  Button,
  useToast,
  Heading,
  Icon,
  useDisclosure,
} from "@chakra-ui/react";
import { HamburgerIcon, CloseIcon, ChevronDownIcon } from "@chakra-ui/icons";
import Link from "next/link";
import Cart from "./Cart";
import { useEffect, useState, useContext } from "react";
import { UserContext } from "../context/UserContext";
import { API_BASE_URL } from "../config";
import axios from "axios";

function Logo(props) {
  return (
    <Box {...props}>
      <Heading fontSize="25pt" fontWeight="bolder">
        {props.visible == 1 && "FACES-21"}
      </Heading>
    </Box>
  );
}

function MenuToggle({ toggle, isOpen }) {
  return (
    <Box
      align="center"
      justify="center"
      display={{ base: "block", md: "none" }}
      onClick={() => {
        if (isOpen == false) {
          document.getElementById("navbar").style.height = "60vh";
          setTimeout(() => toggle(), 200);
        } else {
          document.getElementById("navbar").style.height = "17vh";
          toggle();
        }
      }}
      sx={{ transition: "0.3s" }}
      bg="green.600"
      borderRadius="5px"
      p="5px"
    >
      {isOpen ? <CloseIcon color="white" /> : <HamburgerIcon color="white" />}
    </Box>
  );
}

function MenuItems({ children, isLast, to = "/", ...rest }) {
  return (
    <Link href={to}>
      <Text
        w={{ base: "100%", sm: "auto" }}
        textAlign="center"
        display="block"
        p="5px"
        borderRadius="10px"
        bg={{ base: "green.600", sm: "transparent" }}
        cursor="pointer"
        {...rest}
      >
        {children}
      </Text>
    </Link>
  );
}

function DrawerNavbar({ isOpen }) {
  const [userState, userDispatch] = useContext(UserContext);
  const [loggedIn, setLoggedIn] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const toast = useToast();

  const cart = useDisclosure();

  useEffect(() => {
    console.log(userState.userInfo);
    if (JSON.stringify(userState.userInfo) == "{}") {
      setLoggedIn(false);
    } else {
      setLoggedIn(true);
    }
    setIsLoading(false);
  }, [userState.userInfo]);

  const handleLogout = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/u/auth/logout/`, {
        method: "POST",
        headers: {
          Authorisation: "Token " + userState.userInfo.token,
        },
      });
      // await axios.post(
      //   `${API_BASE_URL}/api/u/auth/logout/`,
      //   {},
      //   {
      //     headers: {
      //       Authorization: "Token " + userState.userInfo.token,
      //     },
      //   }
      // );
      if (res.status == 200) {
        userDispatch({
          type: "REMOVE_USER",
        });
      } else {
        throw new Error(res.statusText);
      }
    } catch (e) {
      console.log(e);
      toast({
        title: "Error logging out",
        status: "error",
        duration: 2000,
        position: "top-right",
      });
    }
  };

  return isLoading ? (
    <></>
  ) : (
    <Box
      display={{ base: isOpen ? "block" : "none", md: "block" }}
      flexBasis={{ base: "100%", md: "auto" }}
      bg={{ base: "green.500", md: "transparent" }}
      p={{ base: "20px", md: "0px" }}
      borderRadius="15px"
    >
      <ScaleFade initialScale={0.5} in={isOpen}>
        <Stack
          spacing={8}
          align="center"
          justify={["center", "space-between", "flex-end", "flex-end"]}
          direction={["column", "row", "row", "row"]}
          pt={[4, 4, 0, 0]}
        >
          <MenuItems
            _hover={{ bg: "rgb(81, 45, 168)" }}
            fontWeight="bold"
            fontSize="15pt"
            to="/"
            sx={{ transition: "background 0.2s" }}
          >
            Home
          </MenuItems>
          {loggedIn && (
            <MenuItems
              _hover={{ bg: "rgb(81, 45, 168)" }}
              fontWeight="bold"
              fontSize="15pt"
              to="/me"
              sx={{ transition: "background 0.2s" }}
            >
              Profile
            </MenuItems>
          )}

          <MenuItems
            _hover={{ bg: "rgb(81, 45, 168)" }}
            fontWeight="bold"
            fontSize="15pt"
            to="/events"
            sx={{ transition: "background 0.2s" }}
          >
            Events
          </MenuItems>

          {!loggedIn ? (
            <Box p="15px" borderRadius="10px">
              <Button
                _hover={{ bg: "rgb(81, 45, 168)" }}
                color="white"
                bg="transparent"
                fontSize="15pt"
                fontWeight="bold"
              >
                <Link href="/login">Login</Link>
              </Button>
            </Box>
          ) : (
            <Box p="15px" borderRadius="10px">
              <Button
                _hover={{ bg: "rgb(81, 45, 168)" }}
                color="white"
                bg="transparent"
                fontSize="15pt"
                fontWeight="bold"
                onClick={handleLogout}
              >
                Logout
              </Button>
            </Box>
          )}
          <Box p="15px" borderRadius="10px">
            <Button
              _hover={{ bg: "rgb(81, 45, 168)" }}
              color="white"
              bg="transparent"
              fontSize="15pt"
              fontWeight="bold"
              onClick={cart.onOpen}
            >
              <Icon />
            </Button>
          </Box>
        </Stack>
      </ScaleFade>
      {loggedIn && (
        <Cart isOpen={cart.isOpen} onClose={cart.onClose} loggedIn={loggedIn} />
      )}
    </Box>
  );
}

const NavbarContainer = (props) => {
  const [background, setBackground] = useState("transparent");
  const { setVisible, ...rest } = props;
  useEffect(() => {
    window.addEventListener("scroll", () => {
      let y = window.scrollY;
      if (y >= 500) {
        setBackground("rgb(17,82,45,0.6)");
        setVisible(1);
      } else {
        setBackground("transparent");
        setVisible(0);
      }
    });
  }, []);

  return (
    <Flex
      as="nav"
      align="center"
      id="navbar"
      justify="space-between"
      wrap="wrap"
      p="20px"
      w="100%"
      background={`${background}`}
      color="white"
      maxH={{ base: "60vh", sm: "25vh", md: "19vh" }}
      sx={{ transition: "background 0.2s " }}
      position="fixed"
      zIndex="1"
      {...rest}
    >
      {props.children}
    </Flex>
  );
};

export default function Navbar(props) {
  const [isOpen, setIsOpen] = useState(true);
  const toggle = () => setIsOpen(!isOpen);
  const [visible, setVisible] = useState(0);

  useEffect(() => {
    window.onresize = () => {
      if (window.innerWidth >= 768) {
        setIsOpen(true);
      } else {
        setIsOpen(false);
      }
    };
    window.innerWidth >= 768 ? setIsOpen(true) : setIsOpen(false);
  }, []);

  return (
    <NavbarContainer setVisible={setVisible} {...props}>
      <Logo
        w="auto"
        visible={visible}
        color={["white", "white", "white", "white"]}
      />
      <MenuToggle toggle={toggle} isOpen={isOpen} />
      <DrawerNavbar isOpen={isOpen} />
    </NavbarContainer>
  );
}
